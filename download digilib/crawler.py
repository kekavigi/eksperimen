import re
import sys
import pickle
import urllib.request as U
from bs4 import BeautifulSoup as bs
from pprint import pprint
from tqdm import tqdm


URL = 'https://digilib.itb.ac.id/index.php/gdl/view/{}'

def dictify(num):
  res = {}

  try:
    with U.urlopen('https://digilib.itb.ac.id/index.php/gdl/view/' + str(num)) as f:
      raw = f.read().decode('utf8', 'ignore')
      soup = bs(raw, 'html.parser')

      tmp = []
      for p in soup.findAll('p')[1:]:
        # pakai try-except karna ada p tanpa class
        # cuma <p>
        try:
          if 'text-left' in p['class']:
            tmp2 = re.sub('(\n|\r|\t)', '', p.decode_contents())
            tmp2 = re.sub(' +', ' ', tmp2)
            tmp.append(tmp2.strip())
        except: pass
      res['judul'] = tmp[0]

      if len(tmp[1]) >= 3:
            res['abstrak'] = tmp[1]

      tmp = soup.findAll('blockquote')[0]
      
      for tr in tmp.findAll('tr'):
        cols = [x.decode_contents() for x in tr.findAll('td')]
        key = cols[0]
        val = re.sub('(<. [^>]*>|<\/.>)', '', cols[2])
        val = re.sub('(\n|\r|\t)', '', val)
        val = re.sub(' +', ' ', val)

        if val!='':
          if key=='Kontributor / Dosen Pembimbing' and len(val) >= 3:
              res['kontributor'] = val

          elif key=='Jenis Koleksi':                 res['jenis'] = val
          elif key=='Penerbit':                      res['penerbit'] = val
          elif key=='Fakultas':                      res['fakultas'] = val
          elif key=='Subjek':                        res['subjek'] = val
          elif key=='Kata Kunci':                    res['kunci'] = val
          elif key=='Tanggal Input':                 res['tanggal'] = val
  
  except: pass
  return res


def batch_download(start, end, batch_size=500):
    for batch in range(start, end+1, batch_size):

        result = {}
        for num in tqdm(range(batch, batch+batch_size), desc=str(batch)):
            result[num] = dictify(num)

        with open('pickle_'+str(num), 'wb') as outfile:
            pickle.dump(result, outfile, -1)


if __name__ == '__main__':
    start = int(sys.argv[1])
    end   = int(sys.argv[2])
    batch_download(start, end)
