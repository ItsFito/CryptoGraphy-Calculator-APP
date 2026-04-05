# Aplikasi Web Kriptografi

Aplikasi web sederhana berbasis **Streamlit** untuk melakukan enkripsi dan dekripsi teks menggunakan beberapa metode kriptografi klasik.

## Fitur

- **Vigenere Cipher** untuk enkripsi dan dekripsi teks.
- **Affine Cipher** untuk enkripsi dan dekripsi teks.
- Menu siap dikembangkan untuk:
  - Playfair Cipher
  - Hill Cipher
  - Enigma Cipher

## Teknologi

- Python
- Streamlit
- NumPy

## Cara Menjalankan

1. Pastikan Python sudah terpasang.
2. Install dependensi:
   ```bash
   pip install streamlit numpy
   ```
3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

## Cara Menggunakan

1. Pilih jenis cipher dari sidebar.
2. Masukkan teks pada kolom input.
3. Pilih mode **Enkripsi** atau **Dekripsi**.
4. Isi parameter yang diperlukan, seperti kunci atau nilai `a` dan `b`.
5. Klik tombol **Proses** untuk melihat hasil.

## Catatan

- Saat ini, yang sudah diimplementasikan di file utama adalah **Vigenere Cipher** dan **Affine Cipher**.
- Cipher lain masih bisa ditambahkan dengan pola fungsi yang sama.

## Informasi Pembuat

Dibuat oleh **Abdullah Fatih Azzam**
