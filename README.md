# Co-Clas: AI-Powered Coffee Bean Grading System

## Tentang Proyek

Proyek ini berangkat dari kebutuhan di lapangan akan alat bantu sortasi kopi yang efisien, terutama untuk petani dan pelaku usaha kecil. Sistem ini memproses gambar biji kopi untuk mendeteksi cacat seperti biji hitam, pecah, keriput, atau berjamur, lalu mengklasifikasikannya berdasarkan mutu standar.

Proses sortasi manual memiliki banyak tantangan, termasuk subjektivitas penilaian dan keterbatasan sumber daya. Dengan sistem berbasis citra, penilaian kualitas dapat dilakukan secara otomatis, akurat, dan konsisten, bahkan dalam skala besar.

## Fitur

- Klasifikasi biji kopi berdasarkan 4 kategori: Dark, Green, Light, dan Medium
- Antarmuka pengguna yang mudah digunakan dengan Streamlit
- Visualisasi hasil prediksi dan tingkat kepercayaan
- Deskripsi karakteristik setiap kelas kualitas

## Instalasi dan Penggunaan

### Prasyarat

- Python 3.7 atau lebih baru
- pip (package manager)

### Langkah Instalasi

1. Clone repositori ini:
```
git clone <url-repositori>
cd Co-Clas
```

2. Instal semua dependensi:
```
pip install -r requirements.txt
```

3. Pastikan file model `model_1.h5` tersedia di direktori yang sama dengan aplikasi.

### Cara Menjalankan Aplikasi

```
streamlit run app.py
```

Aplikasi akan terbuka di browser web Anda secara otomatis.

## Cara Penggunaan

1. Buka aplikasi di browser web
2. Unggah gambar biji kopi yang ingin diklasifikasikan
3. Klik tombol "Analisis Kualitas"
4. Lihat hasil klasifikasi dan deskripsi kualitas kopi

## Hasil Proyek

Proyek ini diharapkan menghasilkan model machine learning yang siap diuji di lapangan atau digunakan untuk pilot project. Hasil akhir akan disetujui oleh tim pengembang serta pihak yang memiliki kompetensi di bidang mutu kopi seperti ahli atau praktisi industri.

## Tim Pengembang

Laskar AI Capstone Project Team

## Lisensi

[MIT License](LICENSE)
