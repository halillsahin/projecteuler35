import sympy

def number(x):
    liste=[]
    a=str(x)*2
    for i in range(len(str(x))):
        liste.append(int(a[i:i+int(len(str(x)))]))
    return liste
asallar=sympy.sieve.primerange(2,1000000)
esasasallar=[]
for i in asallar:
    for a in number(i):
        if not sympy.isprime(a):
            break
    else:
        esasasallar.append(i)
print(len(esasasallar))


    
