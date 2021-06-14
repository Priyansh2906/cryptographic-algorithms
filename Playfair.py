import numpy as np

key = input("Enter a key : ")
rectified_key_letters = "".join(dict.fromkeys(key)) #removes all duplicate letters

alpha=[chr(i) for i in range(97,123)] #Generates a list of all alphabtes 

key_letters = [] #List of letters included in key so that we can know remaining letters to add into 5x5 matrix

for i in rectified_key_letters:
    key_letters.append(i)

for i in key_letters:
    if i=='j':
        key_letters.remove(i)

for i in alpha:
    if i not in key_letters:
        if i =='j':
            pass
        else:
            key_letters.append(i)


print(key_letters)

matrix = np.array(key_letters).reshape(5,5)
print(matrix)

plain_text = input("\n\nEnter plain text : ")
plain_text = plain_text.replace(" ","") #removing blank spaces from plain_text

pairs = [(plain_text[i:i+2]) for i in range(0, len(plain_text), 2)]

#Padding x if there is only one letter in pair
for i in range(0,len(pairs)):
    if len(pairs[i])==1:
        pairs[i] = pairs[i]+'x'     

#Padding x if two letters are same in a pair
for i in range(0,len(pairs)):
    temp_letter = ""
    for letters in pairs[i]:
            if letters==temp_letter:
                    temp_letter = temp_letter+'x'
            else:
                    temp_letter = temp_letter+letters
    pairs[i] = temp_letter
    
print("The pairs are : ",pairs)

position_list = []

for two_letters in pairs:
    position_list_temp = []
    for letter in two_letters:
        row_col = []
        #Iterating the array
        for i in range(0,5):
            for j in range(0,5):
                temp = matrix[i][j]
                if temp == letter:
                    row_col.append(i)
                    row_col.append(j)
                    position_list_temp.append(row_col)
    position_list.append(position_list_temp)
print("positions of each letter are : \n",position_list,"\n\n")

#Main conditions

cipher_text = ""

#0 will be rows
#1 will be coloums

for i in position_list:
    letter1=""
    letter2=""
    #checking if rows are equal
    if i[0][0] == i[1][0]:
        if i[0][1]==4: #if col of only letter 1 is 4 (ending col)
            letter1 = matrix[i[0][0]][i[0][1]-4] #wrapping around
            letter2 = matrix[i[1][0]][i[1][1]+1] #letter2 will be as it is
        elif i[1][1]==4: #if only col of letter2 is 4 (ending col)
            letter1 = matrix[i[0][0]][i[0][1]+1] #letter1 will be as it is
            letter2 = matrix[i[1][0]][i[1][1]-4] #wrapping around
        else:
            letter1 = matrix[i[0][0]][i[0][1]+1]
            letter2 = matrix[i[1][0]][i[1][1]+1]
    
    #checking if cols are equal 
    elif i[0][1] == i[1][1]:
        if i[0][0]==4: #if row of letter1 is 4 (ending row)
            letter1 = matrix[i[0][0]-4][i[0][1]] #wrapping around
            letter2 = matrix[i[1][0]+1][i[1][1]] #as it is
            
        elif i[1][0]==4: #if row of letter2 i 4 (ending row)
            letter1 = matrix[i[0][0]+1][i[0][1]] #as it is
            letter2 = matrix[i[1][0]-4][i[1][1]] #wrapping around
        
        else:
            letter1 = matrix[i[0][0]+1][i[0][1]]
            letter2 = matrix[i[1][0]+1][i[1][1]]
            
    #if neither rows and cols are equal
    else:
        letter1 = matrix[i[0][0]][i[1][1]] #takes same row , different col for letter 1
        letter2 = matrix[i[1][0]][i[0][1]] #takes same row , different col for letter 2
    
    cipher_text=cipher_text+letter1+letter2

print("The encrypted text is : "+cipher_text)
