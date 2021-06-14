import random
import string
alpha=[chr(i) for i in range(97,123)]
setmon=set()
mono=[]
for i in range(26):
  x=random.choice(string.ascii_letters)
  if ( x not in setmon):
    setmon.add(x)
    mono.append(x)
  else:
    x=random.choice(string.ascii_letters)
    setmon.add(x)
    mono.append(x)


plain=input("Enter plain text : ")
encryp=""
decrypt=""
for i in plain:
  encryp+=mono[alpha.index(i)]
for i in encryp:
  decrypt+=alpha[mono.index(i)]

print("The encrypted text is : "+encryp)
print("The decrypted text is : "+decrypt)

