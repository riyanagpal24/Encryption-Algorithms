def gcd(a, b):
    i = 2
    while i<=a and i<=b:
        if(a%i == 0 and b%i == 0):
            gcd = i
            break
        else:
            gcd = 1
            i += 1
    return gcd

e = 2
pt = int(input("Enter plain text> "))
p = int(input("Enter p> ")) 
q = int(input("Enter q> ")) 

n = p*q

prod = (p-1)*(q-1)

while e<prod:
    if gcd(e, prod) == 1:
        break;
    else:
        e += 1
        
ct = pow(pt, e, n)
print("Cipher Text> ",ct)
