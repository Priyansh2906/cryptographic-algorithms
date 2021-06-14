char = [chr(i) for i in range(97,123)]
big_char = [chr(i) for i in range(65,91)]
indexes = [i for i in range(0,27)]

char_dict = dict(zip(char,indexes))
big_char_dict = dict(zip(big_char,indexes))
print(char_dict)
print("\n",big_char_dict)
message = input("Enter message : ")
key = int(input("Enter a key : "))
cipher_text = ""
for i in message:
    if(ord(i)>=97 and ord(i)<=122):
        character_index = char_dict[i]
        #print(character_index)
       
        new_index = character_index+key
        if new_index>25:
            new_index = new_index-26
        for i in char_dict:
            if(char_dict[i]==new_index):
                encrypted_letter = i
                cipher_text = cipher_text+encrypted_letter
    
    if(ord(i)>=65 and ord(i)<=90):
        character_index = big_char_dict[i]
        #print(character_index)
       
        new_index = character_index+key
        if new_index>25:
            new_index = new_index-26
        for i in big_char_dict:
            if(big_char_dict[i]==new_index):
                encrypted_letter = i
                cipher_text = cipher_text+encrypted_letter

print("Cipher text is : ",cipher_text)