
             # 18 encryption and decryption (can be used as a project to *cybersecurity* department)

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f'chars: {chars}')
print(f'key: {key}')

#Encryption
print_word = input('Enter a word to encrypt: ')
cipher_text =''

for letter in print_word:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'your original message was: {print_word}')
print(f'your encrypted message is: {cipher_text}')
print('...........................................')

#Decryption
cipher_text = input('Enter a word to decrypt: ')
print_word =''

for letter in cipher_text:
    index = key.index(letter)
    print_word += chars[index]

print(f"your encrypted message was: {cipher_text}")
print(f' your decrypted message is: {print_word}')
print('..........................................')