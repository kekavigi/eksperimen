# OlahGempa

Ini adalah salah satu *side project* saya. Intinya, saya penasaran apakah kita dapat memprediksi -- dimana, kapan, dan/atau berapa magnitudo -- dari sebuah gempa, jika kita mengetahui hal-hal lain; seperti gempa-gempa yang telah terjadi, pergerakan objek langit seperti bulan, cuaca(?), dkk. Saya berniat mengembangkan AI untuk hal ini, bisa bantu?
*26 Maret 2018*

## Apa yang telah saya lakukan
Dalam proyek ini, saya membuat akun dari [Katalog Gempabumi BMKG](http://repogempa.bmkg.go.id/). Selanjutnya, dengan scraping.py, saya mencoba mendownload **raw data**nya. Jika saya perhatikan, data paling lawas adalah data tahun 2008. Selain itu, sepertinya kode program masih terdapat kesalahan (ada perbedaan antara jumlah data yang ada diserver dengan yang berhasil didownload, namun saya tidak tahu dimana salahnya). Setelah menyimpan file rawnya (yang saya rasa terdapat kesalahan jumlah data), saya menyimpannya di log_gempa.csv.

Apa yang saya ingin lakukan adalah:
- [ ] mengubah CSV ke GeoJSON, dan membuat plot posisi gempa yang telah terjadi di peta.
- [ ] membuat 'timelapse' gempa yang terjadi sejak 1 Januari 2008.
- [ ] membuat plot antar dua variabel, dan beberapa plot hasil analisis lainnya, siapa tau dapat ditemukan sebuah korelasi?
- [ ] membuat AI yang memprediksi gempa.
