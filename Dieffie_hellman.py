'''select a prime number - p
select value of aplha (primitive root of prime number p)
pvt a , pvt_b , public_a,public_b
select random value for pvt a and b less than p
public_a = alpha**pvt_a%p
public_b = alpha**pvt_b%p
key_a = alpha^b^a mod p
key_b = alpha^a^b mod p'''
import random

primes = []
for e in range(1, 100):
   # all prime numbers are greater than 1
   if e > 1:
       for i in range(2, e):
           if (e % i) == 0:
               break
       else:
           primes.append(e)

p = random.choice(primes)
print("Value of prime number p is : ",p)
#Finding alpha as primitive root of p
primitive_roots = []
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

for i in range(1,p):
    if coprime(i,p)==True:
        primitive_roots.append(i)
print(primitive_roots)
print("Relative Primes are : ",primitive_roots) 
alpha = random.choice(primitive_roots)
print("Value of alpha is : ",alpha)

pvt_a = random.randint(2,50)
pvt_b = random.randint(2,50)
print("pvt_a is : ",pvt_a)
print("pvt_b is : ",pvt_b)

public_a = (alpha**pvt_a)%p
public_b = (alpha**pvt_b)%p

print("Public key of a is : ",public_a)
print("Public key of b is : ",public_b)

pvt_key_a = ((alpha**pvt_a)**pvt_b) % p
pvt_key_b = ((alpha**pvt_b)**pvt_a) % p

print("The private key a is : ",pvt_key_a)
print("The private key b is : ",pvt_key_b)

if(pvt_key_a==pvt_key_b):
    print("Key Exchanged!!!")