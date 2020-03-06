# SMS Gateway Pribadi
Beberapa tempat di Indonesia saat ini tidak memiliki akses internet, masih banyak yang mengandalkan SMS dan telepon untuk berkomunikasi. Proyek ini adalah upaya saya untuk tetap dapat mengirimkan dan menerima email, mengakses sosial media -- seperti LINE dan Whatsapps -- Wikipedia, KBBI, WolframAlpha, dan sebagainya, menggunakan SMS lewat handphone klasik seperti Nokia.

*15 May 2018*

## Memulai
### Prasyarat
* Sepertinya tidak ada alamat [SMS Gateway](https://en.wikipedia.org/wiki/SMS_gateway) di Indonesia. Karenanya, diperlukan sebuah server dan nomor telepon yang dapat mentransmisikan dan mengolah SMS. Ada beberapa cara untuk mendapatnya secara gratis -- setidaknya dalam masa trial -- dari beberapa web seperti [Twilio](http://twilio.com/) dan [ClickSend](http://clicksend.com/). Namun cara termudah bagi saya adalah dengan menggunakan [Telerivet](http://telerivet.com/) dan menginstall [Telerivet Gateway App](https://telerivet.com/product/app) pada smartphone Android.
* [Akun Heroku](heroku.com) dan menginstall Heroku CLI. [Ini caranya](https://devcenter.heroku.com/articles/heroku-cli). Ini adalah tempat server nantinya.
* [Akun Github](github.com) dan Git, dan [ini caranya](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
* [Python 3](https://www.python.org/downloads/) untuk bahasa pemrograman yang dipakai. Juga [Pipenv](https://github.com/pypa/pipenv) untuk mengurus module yang akan digunakan.

### Menginstall
Langkah pertama, *clone* repo ini. Selanjutnya install module yang diperlukan, dengan
```console
$ pipenv install
```

app detail

Dan buat app di Heroku
```console
$ heroku create nama-app
```

### Uji Coba.

### Pengembangan

### Lisensi

### Tambahan
