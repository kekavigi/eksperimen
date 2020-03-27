# Simulasi Jalan Raya dengan SUMO

## Instalasi
Saya pakai Ubuntu. Instalasi di Ubuntu mudah. hehehe.
```
sudo -i
add-apt-repository ppa:sumo/stable
apt update && apt install sumo sumo-tools sumo-doc
```
Untuk saya, `sumo --version` adalah 1.5.0

## Data Jalan
1. Dengan menggunakan [tutorial](https://sumo.dlr.de/docs/Tutorials/OSMWebWizard.html), saya mendownload data OSM dari Jl. Taman Sari ITB. 
2. Tentu, tidak semua ruas jalan dipakai, **saya hanya butuh data Jl. Taman Sari, bung**. Di folder hasil download, cari file dengan extension `.net.xml`. itu data network jalan. selanjutnya, `netedit [namafile].net.xml`. perbaiki data :)

## Data Simulasi
3. Ikuti [tutorial](https://sumo.dlr.de/docs/Tutorials/Autobahn.html) untuk membuat simulasi jalan raya.
4. tinggal jalankan, untuk ouput ke XML, ikuti [tutorial](https://sumo.dlr.de/docs/Simulation/Output/RawDump.html), untuk troubleshooting, ada [disini](https://sourceforge.net/p/sumo/mailman/message/35758310/)


# TODO:
1. Atur jenis kendaraan; inflow speed, persentasi jumlah, dkk...
2. Tambahkan obstacle ke jalan, kalau bisa yang 'dinamis' (misal terjadi sekitar 10 menit sekali)
3. Rapikan visualisasi :)
