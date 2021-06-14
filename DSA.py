import sys 
# computing multiplicative inverse
def m_inv(b, n):         
    print("m_inv, b: ", b)
    print("m_inv, n: ", n)
    for z in range(0, n):
        if (((b * z) % n) == 1):
            #print(z)
            return z


def gen_pub_key(g, p, xr):
    y = (g ** xr) % p
    print("PUBlic key ", y)
    return y


def gen_sig(g, p, q, M, k, xr):
    r = ((g ** k) % p) % q
    #print("r: ", r)
    k_inv = m_inv(k, p)
    if k_inv == None:
        print("Inverse cannot be found!!")
        return
    else:
        print("k_inv: ", k_inv)
        s = (int((M + int(xr) * int(r))) * int(k_inv)) % q
        #print("s: ",s)
        return (r, s)


def sig_veri(s, r, p, q, M, g, y):
    #print("sig_veri: p: ", p)
    w = (m_inv(s, p)) % q
    #print("w: ", w)
    u1 = (w * M) % q
    #print("u1: ", u1)
    u2 = (w * r) % q
    #print("u2: ", u2)
    v = (((g * u1) * (y * u2) % p)) % q
    print("v: ", v)
    t = r % q
    if (v == t):
        print("Signature is valid!")
    else:
        print("Signature is not valid!")

p = 303287
q = 151643
g = 252
M = int(input("Enter message : "))#message
M = hash(M)
print("M=",M)
r = 0
s = 0
xr = int(input("Enter Private Key : ")) #private Key
xr = xr % q
k = 1542 #pre message secret number
k = k % q
y = gen_pub_key(g, p, xr)

sig = gen_sig(g,k, p, q,M,xr)
r = int(sig[0])
s = int(sig[1])
print("(r=",str(r),"s=", s,")")
sig_veri(s, r, p, q, M, g, y)