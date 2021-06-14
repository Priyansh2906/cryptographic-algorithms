#No need to create 27x27 matrix!! 
#*****Plain text value + key value % 26 = ciphered text ***** Same as vigenere 
#here only the key will be random
import random 

alpha = [chr(i) for i in range(97,123)]
indexes = [i for i in range(0,26)]

char_dict = dict(zip(alpha,indexes))
print(char_dict)

plain_text = input("\n\nEnter Plain text : ")
plain_text = plain_text.replace(" ","") #removing blank spaces from plain_text

key = ""
while len(key)<len(plain_text):
    temp = random.choice(alpha)
    key = key+temp
    
cipher_text = ""

print("\nRandom key is : "+key)

#encryption using random key
for i in range(0,len(key)):
    index = (char_dict[plain_text[i]] + char_dict[key[i]]) % 26
    for temp in char_dict:
        if(char_dict[temp]==index):
            cipher_text+=temp


print("\nCipher text using auto key is : "+cipher_text)

#for decryption
decrypted_text = ""
for i in range(0,len(key)):
    index = (char_dict[cipher_text[i]] - char_dict[key[i]]) % 26
    for temp in char_dict:
        if(char_dict[temp]==index):
            decrypted_text+=temp
print("Decrypted text is : ",decrypted_text)