# Panduan Instalasi Odoo 18
Ikuti langkah-langkah berikut untuk menginstal dan menjalankan Odoo 18 secara lokal di komputer atau laptop Anda.

---

## Prasyarat
Sebelum memulai instalasi, pastikan Anda telah menginstal perangkat lunak berikut:

- [Git](https://git-scm.com/)
- [Python](https://www.python.org/) (v3.10 ke atas)
- [PostgreSQL](https://www.postgresql.org/) (v14 ke atas)
- [wkhtmltopdf](https://wkhtmltopdf.org/docs.html) *(untuk fitur pencetakan laporan PDF)*

---

## Instalasi

### 1. Clone Repository
Clone repository proyek dari GitHub menggunakan perintah berikut:
```bash
git clone git@github.com:bip-itteam-internal/learn-odoo.git
```

### 2. Masuk ke Direktori Proyek
Pindah ke direktori proyek yang baru saja di-clone:
```bash
cd learn-odoo
```

### 3. Membuat Virtual Environment
Buat environment terpisah untuk menghindari konflik dengan library global:
```bash
python -m venv .env
```

### 4. Aktifkan Virtual Environment
Jalankan perintah berikut sesuai dengan sistem operasi Anda:
- **Windows:**
  ```bash
  .env\Scripts\activate
  ```
- **Linux/macOS:**
  ```bash
  source .env/bin/activate
  ```
Untuk menonaktifkan environment, cukup ketik:
```bash
deactivate
```

### 5. Install Library yang Dibutuhkan
Setelah environment aktif, instal semua library yang diperlukan dengan perintah:
```bash
pip install -r requirements.txt
```

### 6. Konfigurasi File Config
Salin file konfigurasi contoh dan sesuaikan:
```bash
cp odoo.conf.example odoo.conf
```
Edit `odoo.conf` sesuai kebutuhan, termasuk:
- **addons_path**: Lokasi folder `addons` dan `odoo/addons`
- **db_user**: Username untuk PostgreSQL
- **db_password**: Password untuk PostgreSQL
- **admin_passwd**: Master password untuk Odoo

### 7. Menjalankan Odoo
Gunakan perintah berikut untuk menjalankan Odoo:
```bash
python odoo-bin -c odoo.conf
```

### 8. Akses Odoo di Browser
Buka browser dan akses Odoo melalui tautan:
```bash
http://localhost:8022
```
Jika berhasil, Anda akan melihat halaman login Odoo.

---

## Catatan Kekurangan Odoo

### Modul Proyek
Berikut beberapa keterbatasan yang ditemukan dalam modul proyek:
- [Kekurangan 1]
- [Kekurangan 2]
- [Kekurangan 3]

*(Silakan lengkapi daftar kekurangan ini sesuai dengan analisis Anda.)*

---

Selamat mencoba! 🚀