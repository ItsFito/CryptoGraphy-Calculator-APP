import streamlit as st
import numpy as np

# --- FUNGSI LOGIKA CIPHER ---

def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key = key.upper()
    key_idx = 0
    for char in text.upper():
        if char.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord('A')
            if mode == 'encrypt':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_idx += 1
        else:
            result += char
    return result

def affine_cipher(text, a, b, mode='encrypt'):
    # a harus koprim dengan 26
    result = ""
    if mode == 'encrypt':
        for char in text.upper():
            if char.isalpha():
                result += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
            else:
                result += char
    else:
        # Mencari modular multiplicative inverse dari a mod 26
        a_inv = pow(a, -1, 26)
        for char in text.upper():
            if char.isalpha():
                result += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
            else:
                result += char
    return result

# --- ANTARMUKA (UI) ---

st.set_page_config(page_title="Kalkulator Enkripsi Fatih", layout="centered")
st.title("🔐 Aplikasi Web Kriptografi")
st.write("Dibuat oleh: Abdullah Fatih Azzam (NIM: 21120123140118)")

menu = ["Vigenere Cipher", "Affine Cipher", "Playfair Cipher", "Hill Cipher", "Enigma Cipher"]
choice = st.sidebar.selectbox("Pilih Jenis Cipher", menu)

input_text = st.text_area("Masukkan Teks (Plaintext/Ciphertext):")
mode = st.radio("Pilih Mode:", ["Enkripsi", "Dekripsi"])

if choice == "Vigenere Cipher":
    key = st.text_input("Masukkan Kunci (Kata):")
    if st.button("Proses"):
        res = vigenere_cipher(input_text, key, mode.lower())
        st.success(f"Hasil: {res}")

elif choice == "Affine Cipher":
    a = st.number_input("Masukkan Nilai a (Harus ganjil & bukan 13):", value=3, step=2)
    b = st.number_input("Masukkan Nilai b (0-25):", value=5)
    if st.button("Proses"):
        res = affine_cipher(input_text, int(a), int(b), mode.lower())
        st.success(f"Hasil: {res}")

# Untuk Hill, Playfair, dan Enigma, kamu bisa menambahkan fungsinya 
# dengan pola yang sama di atas.