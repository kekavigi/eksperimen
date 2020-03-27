# Simulasi Arus Lalu Lintas

## Menjalankan Simulasi
Dari program SUMO, buka (Ctrl+O) kode simulasi `main.sumocfg`. Ganti pengaturan viewing (F9) dengan menggunakan `viewing.xml`. Selanjutnya tinggal jalankan simulasi :)

![simulasi](screenshot.png)

## Instalasi SUMO
> "Simulation of Urban MObility" (Eclipse SUMO) is an open source, highly portable, microscopic and continuous road traffic simulation package designed to handle large road networks.

Dengan menggunakan [SUMO](https://sumo.dlr.de/docs/), kita dapat mengambil data jalan raya dari OpenStreetMap secara cepat, membuat visualisasi dan data simulasi dengan mudah, dan (dengan menginstall hal lain, seperti [Flow](https://github.com/flow-project/flow)), memungkinkan meningkatkan kompleksitas simulasi. Untuk Ubuntu, SUMO dapat diinstall dengan
```
sudo -i
add-apt-repository ppa:sumo/stable
apt update && apt install sumo sumo-tools sumo-doc
```

Versi SUMO (dapat dicari dengan menjalankan `sumo --version`) yang dipakai pada proyek ini adalah 1.5.0


## Mendapatkan Data Jalan Raya
SUMO telah memberikan [tutorial sederhana]((https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html)) bagaimana mendapatkan data jalan raya dari Open Street Map (OSM). SUMO juga menyediakan `netedit`, program GUI yang memungkinkan merapikan data yang diambil dari OSM.


## Data Simulasi
Sekali lagi, SUMO menyediakan [tutorial](https://sumo.dlr.de/docs/Tutorials/Autobahn.html) untuk membuat simulasi jalan raya, dan [tutorial](https://sumo.dlr.de/docs/Simulation/Output/RawDump.html) untuk output ke XML. Untuk troubleshooting, ada [disini](https://sourceforge.net/p/sumo/mailman/message/35758310/).



# TODO:
- [ ] Pada data jalan, kedua ujung jalan perlu diperpanjang beberapa belas/puluh meter. Hal ini dilakukan untuk memberi ruang (dan waktu) bagi setiap kendaraan untuk berakselerasi. Kita config yang memungkinkan setiap kendaraan yang di-spawn pada awalnya melaju dengan kecepatan maksimum?
- [ ] tambahkan Car Following Model
- [ ] Atur jenis kendaraan; inflow speed, persentasi jumlah, dkk...
- [ ] Tambahkan obstacle ke jalan, kalau bisa yang 'dinamis' (misal terjadi sekitar 10 menit sekali)
- [ ] Rapikan visualisasi :)
