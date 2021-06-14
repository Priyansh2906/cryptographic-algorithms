#No need to create 27x27 matrix!! 
#*****Plain text value + key value % 26 = ciphered text *****

alpha = [chr(i) for i in range(97,123)]
indexes = [i for i in range(0,26)]

char_dict = dict(zip(alpha,indexes))
print(char_dict)

plain_text = input("\n\nEnter Plain text : ")
plain_text = plain_text.replace(" ","") #removing blank spaces from plain_text

key = input("Enter a unique key to encrypt : ")
auto_key = key
repeated_key = key
cipher_text = ""
repeated_cipher_text = ""

#forming final key using autokey system
if len(key)<len(plain_text):
    for i in range(0,len(plain_text)):
        if len(auto_key)==len(plain_text):
            break
        else:
            auto_key = auto_key+plain_text[i]
            

#forming final key using repeated key system
while len(repeated_key)<len(plain_text):
    for i in range(0,len(key)):
        if len(repeated_key)==len(plain_text):
            break
        else:
            repeated_key = repeated_key+key[i]

print("\n\nFinal key using autokey is : "+auto_key)
print("Final key using repeated is : "+repeated_key)

#encryption using auto_key
for i in range(0,len(auto_key)):
    index = (char_dict[plain_text[i]] + char_dict[auto_key[i]]) % 26
    for temp in char_dict:
        if(char_dict[temp]==index):
            cipher_text+=temp

#encryption using repeated_key
for i in range(0,len(repeated_key)):
    index = (char_dict[plain_text[i]] + char_dict[repeated_key[i]]) % 26
    for temp in char_dict:
        if(char_dict[temp]==index):
            repeated_cipher_text+=temp

print("\n\nCipher text using auto key is : "+cipher_text)
print("Cipher text using repeated key is : "+repeated_cipher_text)
