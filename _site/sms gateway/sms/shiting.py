from django.http import HttpResponse
from urllib.parse import quote
from bs4 import BeautifulSoup
from re import sub
import sms.telerivet as telerivet
import wikipedia
import requests
import smtplib
import json

EMAIL_USERNAME      = "someone@somewhere.com"
EMAIL_PASSWORD      = "EmailPassword"
PHONE_NUMBER        = "+62xxxxxxxxxxx"
WOLFRAM_APPID       = "AppID"
TELERIVET_API_KEY   = "APIKey"
TELERIVET_PROJECT_ID= "ProjectID"

# atur bahasa wikipedia
wikipedia.set_lang('en')

def replier(Input):
    """Memberikan response kepada server Telerivet."""
    message = {'messages': [{'content': Input}]}
    return HttpResponse(json.dumps(message),'application/json')

def keyword_email(Input):
    """Mengirimkan email ke seseorang."""
    try:
        (TO, SUBJECT, TEXT) = Input
    except:
        return 'data tidak lengkap'

    message = """From: {}\nTo: {}\nSubject: {}\n\n{}""".format(EMAIL_USERNAME, TO, SUBJECT, TEXT)

    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()
    server.ehlo_or_helo_if_needed()
    try:
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, TO, message)
        server.close()
        return 'Email terkirim.'
    except:
        return 'Email gagal terkirim.'

def keyword_wiki(Input):
    """Memberikan rangkuman Wikipedia."""
    try:
        # coba dapatkan rangkuman wikipedia
        summary = wikipedia.summary(Input,sentences=2)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # kalau ada error, sampaikan kemungkinannya
        text = 'Ambigu:\n'
        for x in e.options:
            text += x + '\n'
        return text[:-1]

def keyword_wolf(Input):
    """Memberikan hasil WolframAlpha."""
    # dapatkan hasil raw dari WolframAlpha
    query = 'https://api.wolframalpha.com/v2/query?input=' + quote(Input) + '&format=plaintext&output=JSON&appid=' + WOLFRAM_APPID
    temp = requests.get(query)
    temp = temp.json()['queryresult']

    # hasil tersimpan pada key 'pods'
    if 'pods' not in temp:
        return 'kesalahan interpretasi'
    else:
        pods = temp['pods']
        # gabungkan semua hasil dalam satu string
        text = ''
        #perlu ditetapkan maksimal jawaban, agar SMS yang terkirim tidak banyak.
        for x in range(min(7, len(temp))):
            subpods = pods[x]['subpods']
            for y in range(len(subpods)):
                if subpods[y]['plaintext'] != '':
                    text += subpods[y]['plaintext'] + '\n'
        #formatting kecil
        text = text[:-1].replace('  ', ' ')
        return text

def keyword_trans(Input):
    """Memberikan hasil Google Translate kepada EMAIL_USERNAME."""
    #contoh Input = "en id TEKS YANG MAU DIUBAH"
    #ganti spasi diantara dua kode bahasa
    lang_id = Input[:5].replace(' ', '&tl=')
    query = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + lang_id + '&dt=t&q=' + quote(Input[6:])
    text = requests.get(query)
    text = text.json()[0][0][0]
    return text

def keyword_kbbi(Input):
    """Memberikan hasil Pusat Bahasa."""
    # ambil data dari website KBBI
    r   = requests.get('https://kbbi.kemdikbud.go.id/entri/'+Input)
    # lakukan beberapa formatting
    soup= str(BeautifulSoup(r.text,"html5lib")).split('<hr/>')[1]
    soup= sub('<sup>'               ,'^',soup).replace('</sup>' , '')
    soup= sub('<span[\w":=, ]*">' ,'{',  soup).replace('</span>','}')
    soup= sub('<a href="[./a-z]*">' ,'' ,soup)
    soup= sub('<[\w /":;=-]*>'      ,'' ,soup)
    soup= sub(' +'                  ,' ',soup)
    soup= soup.split('\n')

    text= ''
    for char in soup:
        if char not in ['',' ']:
            text += char+'\n'
    if 'Entri tidak ditemukan.' in text:
        text = 'Entri tidak ditemukan. '
    return(text[:-1])

def keyword_ifttt(Input):
    """Memberikan hasil dari IFTTT."""
    tr = telerivet.API(TELERIVET_API_KEY)
    tr = tr.initProjectById(TELERIVET_PROJECT_ID)

    tr.sendMessage(to_number=PHONE_NUMBER, content=Input)
    return None
    
def keyword(ID, content):
    """Mengeksekusi keyword yang dipilih."""
    menu = {'Email': keyword_email, 'Kbbi' : keyword_kbbi, 'Wiki' : keyword_wiki, 'Trans': keyword_trans, 'Wolf':keyword_wolf, 'ifttt':keyword_ifttt}

    # menyederhanakan isi variabel content
    if len(content)==1:
        content=content[0]
    if ID in menu:
        #batasi agar tidak melebihi 300 karakter
        result = menu[ID](content)[:300]
    else:
        result = None
    return replier(result)
