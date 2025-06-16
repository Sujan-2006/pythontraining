import random
import string
chars=list(" "+string.punctuation + string.digits +string.ascii_letters)
key=chars.copy()
random.shuffle(key)
print(f"chars: {chars}")
print(f"key: {key}")

#ENCRYPT

text=input("enter a message to encrypt : ")
ciphertext=""

for letter in text:
    i=chars.index(letter)

    ciphertext+=key[i]
print(f"original message : {text}")
print(f"encrypted message : {ciphertext}")


#DECRYPT

ciphertext=input("enter a message to Decrypt : ")
text=""

for letter in ciphertext:
    i=key.index(letter)
    text+=chars[i]

print(f"encrypted message : {ciphertext}")
print(f"original message : {text}")



    