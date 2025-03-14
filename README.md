# Panduan Instalasi Odoo 18
Ikuti langkah-langkah berikut untuk mengatur aplikasi secara lokal di komputer atau laptop Anda.

## Prasyarat
* [Git](https://git-scm.com/)
* [Python](https://www.python.org/) (v3.10 ke atas)
* [PostgresSQL](https://www.postgresql.org/) (v14 ke atas)
* [wkhtmltopdf](https://wkhtmltopdf.org/docs.html)

## Instalasi
1. **Clone Repository**  
   Clone repository proyek dari GitHub melalui terminal. Anda dapat memilih menggunakan tautan `HTTP` atau `SSH` dengan perintah berikut:
   ```bash
   git clone git@github.com:bip-itteam-internal/learn-odoo.git
   ```

2. **Masuk ke Direktori Proyek**  
   Pindah ke direktori proyek yang baru saja di-clone:
   ```bash
   cd learn-odoo
   ```

3. **Membuat Environment**  
   Sebelum menginstal library yang dibutuhkan, sebaiknya membuat environment terpisah dari environment global supaya tidak bentrok. Untuk membuatnya, gunakan perintah berikut:
   ```bash
   python -m venv .env
   ```

4. **Aktifkan Environment**  
   Untuk mengaktifkan environment yang telah dibuat, gunakan perintah berikut:
   ```bash
   .env/Scripts/activate
   ```
   Sedangkan untuk menonaktifkan environment, cukup ketik perintah berikut di terminal:
   ```bash
   deactivate
   ```

5. **Install Library**  
   Setelah berhasil membuat environment, jalankan perintah berikut untuk menginstal semua library yang dibutuhkan oleh aplikasi:
   ```bash
   pip install -r requirements.txt
   ```

6. ****

6. **Menjalankan Proyek**  
   Untuk menjalankan odoo, cukup gunakan perintah berikut:
   ```bash
   python odoo-bin -c odoo.conf
   ```

7. **Buka Browser**  
   Gunakan browser kesayangan Anda untuk menjalankan sistem ini, kemudian buka tautan berikut:
   ```bash
   http://localhost:8022
   ```

   ----
   
# Catatan Kekurangan Odoo

## Modul Poryek
* Lorem Ipsum
* Lorem Ipsum
* Lorem Ipsum