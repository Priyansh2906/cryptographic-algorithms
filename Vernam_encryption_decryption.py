#cipher text = (plain_text + key) % 26
import random

alpha = [chr(i) for i in range(97,123)]
indexes = [i for i in range(0,26)]

character_dict = dict(zip(alpha,indexes))
print(character_dict)

plain_text = input("\n\nEnter the Plain text : ")
plain_text = plain_text.replace(" ","") #removing the blank spaces

key = ""

while len(key)<len(plain_text):
    temp = random.choice(alpha)
    key = key+temp
    
print("Randomly generated key is : "+key)

cipher_text = ""

#encryption using random key

for i in range(0,len(key)):
    index = (character_dict[plain_text[i]]+character_dict[key[i]]) % 26
    for temp in character_dict:
        if(character_dict[temp]==index):
            cipher_text+=temp

print("The Cipher text is : "+cipher_text)

#decrypting using the random key

decrypted_text = ""

for i in range(0,len(key)):
    index = (character_dict[cipher_text[i]] - character_dict[key[i]])%26
    for temp in character_dict:
        if(character_dict[temp]==index):
            decrypted_text+=temp
            
print("The decrypted text is : "+decrypted_text)