import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
print("Character set:", chars)
print("Shuffled key :", key)

plain_text = input("Enter a message to encrypt: ")  # original text
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"\nOriginal message : {plain_text}")
print(f"Encrypted message: {cipher_text}")
