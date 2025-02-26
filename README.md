# Chatbot UI dengan Streamlit dan LM Studio

## Deskripsi Proyek

Proyek ini adalah antarmuka chatbot sederhana menggunakan Streamlit yang menghubungkan model bahasa besar (LLM) yang tersedia di LM Studio. Chatbot ini dapat berkomunikasi dengan pengguna dan memberikan respons yang relevan sesuai dengan input yang diberikan.

## Fitur Utama

- **Antarmuka Sederhana**: Menggunakan Streamlit untuk membuat UI chatbot.
- **Integrasi dengan LM Studio**: Memanfaatkan model bahasa besar yang berjalan di lokal.
- **Streaming Respon**: Menampilkan jawaban chatbot secara real-time.
- **Menyimpan Riwayat Chat**: Percakapan sebelumnya tetap tersedia selama sesi aplikasi berjalan.

## Instalasi

### Persyaratan

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal:

- **Python** (>=3.8)
- **LM Studio** (dengan model yang telah dikonfigurasi)
- **Paket Python yang diperlukan**

### Cara Install

1. **Clone Repository**
  ```bash
  git clone https://github.com/username/repo-name.git
  cd repo-name
  ```

2. **Buat Virtual Environment** (Opsional tetapi direkomendasikan)
  ```bash
  python -m venv venv
  source venv/bin/activate  # Untuk Linux/Mac
  venv\Scripts\activate  # Untuk Windows
  ```

3. **Instal Dependensi**
  ```bash
  pip install -r requirements.txt
  ```

4. **Konfigurasi LM Studio**
  Pastikan LM Studio sudah berjalan dan model telah dimuat.
  Gunakan URL lokal yang sesuai untuk API LM Studio (default: http://127.0.0.1:1234/v1).

5. **Jalankan Aplikasi**
   ```bash
   streamlit run chatbot.py
   ```

## Penggunaan

1. **Buka browser dan akses alamat yang ditampilkan oleh Streamlit.**
2. **Mulai percakapan dengan chatbot.**
3. **Riwayat chat akan tetap tersedia selama sesi berjalan.**

## Struktur Kode

|-- chatbot.py  # Kode utama aplikasi
|-- requirements.txt  # Daftar dependensi
|-- README.md  # Dokumentasi proyek

## Pengembang

**Nama:** Abulkhair Rizvan Yahya  
**Email:** [aburnyh.yahya@gmail.com](mailto:aburnyh.yahya@google.com)  
**LinkedIn:** [linkedin.com/in/arizvanyahya](https://linkedin.com/in/arizvanyahya)

