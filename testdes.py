import streamlit as st
import pycryptodome
from Crypto.Cipher import DES

def pad_message(message):
    while len(message) % 8 != 0:
        message += ' '
    return message

def unpad_message(message):
    return message.rstrip()

def generate_key(key):
    return DES.new(key.encode('utf-8'), DES.MODE_ECB)

def encrypt_message(text, cipher):
    padded_text = pad_message(text)
    encrypted_text = cipher.encrypt(padded_text.encode('utf-8'))
    return encrypted_text

def decrypt_message(encrypted_text, cipher):
    decrypted_text = cipher.decrypt(encrypted_text)
    return unpad_message(decrypted_text.decode('utf-8'))

def main():
    st.title("🔑 ## DES Cryptography 🔑")
    
    with st.expander("Lebih lanjut mengenai DES!"):
        st.markdown(
            """
            DES adalah salah satu dari contoh Algoritma kriptografi modern.
            \nDES Merupakan data dienkripsi dalam blok 64-bit menggunakan kunci internal 56-bit yang dibangkitkan dari kunci eksternal 64-bit.
            """
        )

    col1, col2 = st.columns(2)

    # Enkripsi pesan
    with col1:
        st.subheader("Enkripsi pesan")
        key = st.text_input("Masukkan kunci 8 karakter:")
        if len(key) != 8:
            st.warning("Masukkan kunci dengan maksimal 8 karakter (contoh: 00000000)")
            st.stop()
        text = st.text_area("Masukkan pesan untuk dienkripsi")
        encrypt_button = st.button("Encrypt")

        if text == "":
            st.warning("Kotak enkripsi pesan tidak boleh kosong")

        if encrypt_button:
            cipher = generate_key(key)
            try:
                encrypted_message = encrypt_message(text, cipher)
                st.write("Encrypted message: ", encrypted_message.hex())
            except:
                st.warning("Pesan terlalu besar, harap masukkan pesan yang lebih kecil atau gunakan kunci yang lebih besar.")

    # Dekripsi pesan
    with col2:
        st.subheader("Dekripsi pesan")
        encrypted_message_input = st.text_area("Masukkan pesan terenkripsi")
        decrypt_button = st.button("Decrypt")

        if encrypted_message_input == "":
            st.warning("Masukkan pesan untuk didekripsi")

        try:    
            if decrypt_button:
                cipher = generate_key(key)
                decrypted_message = decrypt_message(bytes.fromhex(encrypted_message_input), cipher)
                st.write("Decrypted message: ", decrypted_message)
        except:
            st.warning("Tidak bisa di dekripsi.")

    st.info("Setiap kali melakukan enkripsi, key akan digenerate secara otomatis. Silakan copy private key untuk melakukan dekripsi.")

    st.write("Kelompok 7 DES Kriptografi © 2023")

if __name__ == "__main__":
    main()
