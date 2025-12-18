# KID Project
Project ini mensimulasikan layanan security server sederhana dalam bahasa Python.

Anggota Kelompok : 
1. Yanaka Sofia Pardede (24031554065)
2. Annisa Ramadhani (24031554206)
3. Arya abdi wicaksana (24031554224)

Deskripsi Proyek :
Proyek ini merupakan pengembangan layanan Punk Records API yang menerapkan konsep kriptografi dan keamanan sistem untuk menjamin integritas, autentikasi, dan kerahasiaan data. Sistem dibangun secara bertahap mengikuti skema penilaian York, Edison, Pythagoras (B+), hingga Stella (A), dengan fitur utama meliputi penyimpanan public key, verifikasi signature digital, pengiriman pesan terenkripsi, serta penandatanganan dokumen PDF. Pada tahap akhir, sistem dilengkapi mekanisme secure session menggunakan token Bearer (JWT) untuk membatasi akses endpoint hanya kepada pengguna terautentikasi. Seluruh fungsi diimplementasikan berbasis REST API dan diuji melalui Swagger UI untuk memastikan sistem berjalan aman, konsisten, dan sesuai dengan kebutuhan keamanan modern.

# Instalasi
1.  Pasang uv from [situs resmi](https://docs.astral.sh/uv/getting-started/installation/).
2.  Persipakan project ini dengan melakukan sinkronisasi dependensi. Ketik `uv sync` pada terminal di lokasi project ini berada. Perintah ini akan membuat sebuah virtual environment `.venv` (hidden) pada root folder, lalu memasang libraries yang dibutuhkan.
3.  Untuk menjalankan server FastAPI, ketik perintah:
```
uv run main.py
```
Untuk penggunaan lainnya, lihat bab Penggunaan.

# Petunjuk Penggunaan dan Informasi API keseluruhan
1.  Menjalankan server FastAPI
```
uv run main.py
```
2.  Mengakses antarmuka API (seperti [Postman](https://www.postman.com/) atau [Bruno](https://www.usebruno.com/)) dapat melalui platform bawaan FastAPI, yaitu `SwaggerAPI` dengan cara:
```
http://localhost:8080/docs
```
3.  Laman `SwaggerAPI` (http://localhost:8080/docs) akan menampilkan seluruh fungsi-fungsi API yang telah anda buat dalam file `api.py`.
    -   Klik pada fungsi yang akan diakses.
    -   Klik `Try it out`
    -   Lengkapi formulir (parameters fungsi) yang dibutuhkan.
    -   Klik `Execute` untuk melakukan "submission".
