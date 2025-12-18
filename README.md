# KID Project
Project ini mensimulasikan layanan security server sederhana dalam bahasa Python.

Anggota Kelompok : 
1. Yanaka Sofia Pardede (24031554065)
2. Annisa Ramadhani (24031554206)
3. Arya abdi wicaksana (24031554224)

Deskripsi Proyek :
Proyek ini bertujuan untuk membangun sebuah sistem Punk Records API yang menerapkan prinsip dasar hingga lanjutan dalam bidang kriptografi dan keamanan informasi. Pengembangan sistem dilakukan secara bertahap mengikuti skema penilaian York, Edison, Pythagoras (B+), dan Stella (A). Pada tahap awal, sistem menyediakan fungsi dasar seperti penyimpanan public key, verifikasi signature, relay message, serta penandatanganan dokumen PDF. Selanjutnya, sistem dikembangkan dengan penambahan mekanisme integrity check, multiuser, dan variasi penggunaan cipher untuk meningkatkan fleksibilitas dan keandalan sistem.

Pada tahap akhir (Stella), sistem dilengkapi dengan mekanisme secure session menggunakan token Bearer berbasis JSON Web Token (JWT). Mekanisme ini memastikan bahwa setiap endpoint penting hanya dapat diakses oleh pengguna yang telah terautentikasi dan terotorisasi. Implementasi secure session ini meningkatkan tingkat keamanan sistem dengan membatasi akses tidak sah serta memastikan setiap proses komunikasi dilakukan dalam sesi yang aman. Seluruh fitur diuji menggunakan Swagger UI untuk memastikan fungsionalitas berjalan dengan baik dan sesuai dengan kriteria keamanan yang ditetapkan.

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
