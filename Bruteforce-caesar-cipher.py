str = input("Enter cipher text : ")

key=0

for key in range(1,27):
    decrypted_text = ''
    for i in str:
        ascii_val = ord(i)
        
        
        temp_ascii = ascii_val-key
            #Checking if it is small alphabet or capital aplhabet
        if ascii_val>=65 and ascii_val<=90:
            #Capital letter
            if temp_ascii<65:
                ascii_val = (temp_ascii + 26)
            else:
                ascii_val = ascii_val - key
            decrypted_text = decrypted_text+chr(ascii_val)
                
        if(ascii_val>=97 and ascii_val<=122):
            #small letter 
            temp_ascii = ascii_val-key
            if temp_ascii<97:
                ascii_val = (temp_ascii + 26) 
            else:
                ascii_val = ascii_val - key
            decrypted_text = decrypted_text+chr(ascii_val)
            
    print(decrypted_text)
    key = key+1