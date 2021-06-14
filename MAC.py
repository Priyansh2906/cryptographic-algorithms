import random 

alpha = [chr(i) for i in range(97,123)]
indexes = [i for i in range(0,26)]

char_dict = dict(zip(alpha,indexes))
print(char_dict)

plain_text = input("\n\nEnter Plain text : ")
plain_text = plain_text.replace(" ","") #removing blank spaces from plain_text

key = input("Enter a unique key to encrypt : ")
auto_key = key
if len(key)<len(plain_text):
    for i in range(0,len(plain_text)):
        if len(auto_key)==len(plain_text):
            break
        else:
            auto_key = auto_key+plain_text[i]
    


print("\nGenerated key is : "+auto_key)
cipher_text = ""
for i in range(0,len(auto_key)):
    index = (char_dict[plain_text[i]] + char_dict[auto_key[i]]) % 26
    for temp in char_dict:
        if(char_dict[temp]==index):
            cipher_text+=temp

print("\nCipher text using auto key is : "+cipher_text)

plain_text = plain_text+"XX"
plain_text = plain_text+cipher_text
print("Resultant plain text after cipher : ",plain_text)

recieved_message = plain_text
recieved_plaint_text = recieved_message.split('XX',1)[0]
recieved_cipher = recieved_message.split('XX',1)[1]

print("Recieved plain text is : ",recieved_plaint_text)
print("Recieved Cipher text is : ",recieved_cipher)

resultant_cipher=""

#Encrypting again the recieved plain text
new_key = key
new_auto_key = new_key
if len(new_key)<len(recieved_plaint_text):
    for i in range(0,len(recieved_plaint_text)):
        if len(new_auto_key)==len(recieved_plaint_text):
            break
        else:
            new_auto_key = new_auto_key+recieved_plaint_text[i]
    
print("\Generated key is : "+auto_key)
for i in range(0,len(auto_key)):
    index = (char_dict[recieved_plaint_text[i]] + char_dict[auto_key[i]]) % 26
    for temp in char_dict:
        if(char_dict[temp]==index):
            resultant_cipher+=temp

if(resultant_cipher==recieved_cipher):
    print("Both Cipher texts match!! Message authenticated successfully!!")