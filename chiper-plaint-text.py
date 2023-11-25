import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# Proses enkripsi
plain_text = input("Masukkan Pesan yang Ingin Di-Enkripsi: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print("Pesan original:", plain_text)
print("Hasil enkripsi:", cipher_text)

# Proses dekripsi
cipher_text = input("Masukkan pesan yang ingin Di-Dekripsi: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print("Pesan Enkripsi:", cipher_text)
print("Pesan Original:", plain_text)
