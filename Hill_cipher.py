import numpy as np

alpha = [chr(i) for i in range(97,123)]
indexes = [int(i) for i in range(0,26)]
char_dict = dict(zip(alpha,indexes))
key_list = []
indexed_key_list = []

print("The characters are numbered/indexed in the following order : \n",char_dict)

key = input("\n\nEnter a key (must be of 4 or 9 letters only!!) : ")

for i in key:
    key_list.append(i)

for i in key:
    indexed_key_list.append(char_dict[i])
    

if len(key)==4:
    key_array = np.array(key_list).reshape(2,2)
    indexed_key_array = np.array(indexed_key_list).reshape(2,2)
    
if len(key)==9:
    key_array = np.array(key_list).reshape(3,3)
    indexed_key_array = np.array(indexed_key_list).reshape(3,3)
    
print("\n\nThe key is : "+key)
print("\nThe key array is : \n",key_array)
print("\nThe indexed key array is : \n",indexed_key_array)

plain_text = input("\n\n Enter plain text : ")
plain_text = plain_text.replace(" ","") #removing blank spaces from plain_text

if len(key)==4:
    #Pair the plain text letters in a pair of 2
    pairs = [(plain_text[i:i+2]) for i in range(0, len(plain_text), 2)]
    for i in range(0,len(pairs)):
        if len(pairs[i])==1:
            temp=pairs[i]+'x'
            pairs[i]=temp


if len(key)==9:
    #Pair the plain text letter in a pair of 3
    pairs = [(plain_text[i:i+3]) for i in range(0, len(plain_text), 3)]
    for i in range(0,len(pairs)):
        if len(pairs[i])==1:
            temp = pairs[i]+'x'
            temp = pairs[i]+'x'
            pairs[i] = temp

        if len(pairs[i])==2:
            temp = pairs[i]+'x'
            pairs[i]=temp
            

print("The pairs are : ",pairs)

indexed_pair_array = []

#indexing each letter in each pair
for i in range(0,len(pairs)):
    temp_indexed_pair_array = []
    for character in pairs[i]:
        temp = char_dict[character]
        temp_indexed_pair_array.append(temp)
    indexed_pair_array.append(temp_indexed_pair_array)
print(indexed_pair_array)

for i in range(0,len(indexed_pair_array)):
    temp = np.array(indexed_pair_array[i])
    indexed_pair_array[i]=temp

print("All the arrays for plain text are : \n",indexed_pair_array)

cipher_text = ""
result = []

for i in range(0,len(indexed_pair_array)):
    temp = np.matmul(indexed_key_array,indexed_pair_array[i])
    temp = temp%26
    #extracting letters from resultant product
    for i in range(0,len(temp)):
        ans_temp = temp[i]
        result.append(ans_temp)

print("The resultant cipher indexes are : ",result)
for i in result:
    for alphabet in char_dict:
        if(char_dict[alphabet]==i):
            cipher_text=cipher_text+alphabet

print("Cipher text is : "+cipher_text)

#Now decrypting the cipher text from the entered key , back to plain text
#Decryption is P = C*K^-1 mod 26

print("\n\n\n**********Decryption**********")

#finding inverse of the key matrix
inverse_key_matrix = indexed_key_array
print("inverse_key_matrix = 1/ad-cb * ",np.array([inverse_key_matrix[1][1],-inverse_key_matrix[0][1],-inverse_key_matrix[1][0],inverse_key_matrix[0][0]]).reshape(2,2))
adjoint_array = np.array([inverse_key_matrix[1][1],-inverse_key_matrix[0][1],-inverse_key_matrix[1][0],inverse_key_matrix[0][0]]).reshape(2,2)
ad_cb = (inverse_key_matrix[0][0] * inverse_key_matrix[1][1]) - (inverse_key_matrix[1][0] * inverse_key_matrix[0][1])
print("ad-cb is : ",ad_cb)
ad_cb=ad_cb%26
print("ad-cb % 26 is : ",ad_cb)

#now modulo 26 the [d -b -c a]
adjoint_array = adjoint_array%26
print("adjoint array % 26 is : ",adjoint_array)

#now find multiplicative inverse of ad_cb
multiplicative_inverse = 0
i = ad_cb
mod = 26
for x in range(1,100):
    y = (i*int(x))%mod
    if y==1:
        print("multiplicative inverse of ",ad_cb," is ",x)
        multiplicative_inverse = x
        break
#now numtiply inverse into adjoint_array and then mod them by 26
inverse_key_matrix = (multiplicative_inverse * adjoint_array).reshape(2,2) % 26
print("inverse_key_matrix is : ",inverse_key_matrix)

#Making pairs of cipher text as we did with plain text and indexing it
if len(key)==4:
    #Pair the plain text letters in a pair of 2
    pairs = [(cipher_text[i:i+2]) for i in range(0, len(cipher_text), 2)]
    for i in range(0,len(pairs)):
        if len(pairs[i])==1:
            temp=pairs[i]+'x'
            pairs[i]=temp


if len(key)==9:
    #Pair the plain text letter in a pair of 3
    pairs = [(cipher_text[i:i+3]) for i in range(0, len(cipher_text), 3)]
    for i in range(0,len(pairs)):
        if len(pairs[i])==1:
            temp = pairs[i]+'x'
            temp = pairs[i]+'x'
            pairs[i] = temp

        if len(pairs[i])==2:
            temp = pairs[i]+'x'
            pairs[i]=temp
            

print("The pairs are of cipher text are : ",pairs)

#indexing each letter in the pair
indexed_pair_array = []

for i in range(0,len(pairs)):
    temp_indexed_pair_array = []
    for character in pairs[i]:
        temp = char_dict[character]
        temp_indexed_pair_array.append(temp)
    indexed_pair_array.append(temp_indexed_pair_array)
print(indexed_pair_array)

for i in range(0,len(indexed_pair_array)):
    temp = np.array(indexed_pair_array[i]).reshape(2,1)
    indexed_pair_array[i]=temp

print("All the arrays for cipher text are : \n",indexed_pair_array)

#Decrypting

plain_text = ""
result = []

print("multiplying matricies : ")

for i in range(0,len(indexed_pair_array)):
    temp = np.matmul(inverse_key_matrix,indexed_pair_array[i])
    print("matrix multiplication is : ",temp)
    temp = temp%26
    #extracting letters from resultant product
    for i in range(0,len(temp)):
        ans_temp = temp[i]
        result.append(ans_temp)

print("The resultant cipher indexes are : ",result)
for i in result:
    for alphabet in char_dict:
        if(char_dict[alphabet]==i):
            plain_text=plain_text+alphabet

print("The decrypted Plain text is : "+plain_text)

