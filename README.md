# Building-a-Simple-ETL-Pipeline

## Deskripsi Proyek

Proyek ini mengimplementasikan proses **ETL (Extract, Transform, Load)** untuk mengolah data produk fashion yang diperoleh dari website Fashion Studio Dicoding. Pipeline ini melakukan pengambilan data (scraping), pembersihan serta normalisasi data, kemudian menyimpan hasilnya ke berbagai media penyimpanan.

## Fitur Utama

### 1. Extract

Mengambil data produk fashion secara otomatis melalui proses web scraping dari website https://fashion-studio.dicoding.dev.

### 2. Transform

Melakukan proses pembersihan dan transformasi data, meliputi:

* Konversi harga produk ke format numerik (IDR).
* Ekstraksi informasi rating dan warna produk.
* Pembersihan serta normalisasi nama produk.
* Penghapusan data duplikat.
* Penanganan nilai yang hilang (missing values).

### 3. Load

Menyimpan data yang telah ditransformasikan ke beberapa tujuan penyimpanan:

* CSV File
* Google Spreadsheet
* PostgreSQL Database

## Cara Menjalankan Proyek

### Instalasi Dependensi

```bash
pip install -r requirements.txt
```

### Menjalankan ETL Pipeline

```bash
python main.py
```

### Menjalankan Unit Test

```bash
python -m pytest tests
```

### Menjalankan Test Coverage

```bash
coverage run -m pytest tests
```
PERLU DIINGAT!!
File google-sheets-api.json sangat diperlukan

## Google Spreadsheet

Hasil data yang telah diproses dapat dilihat melalui Google Spreadsheet berikut:
https://docs.google.com/spreadsheets/d/1fM5gTCmhkmEBY783m7FW4B1lWc7oSj3jQxvpDff8oyk/edit?gid=0#gid=0
