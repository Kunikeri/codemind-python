import math
n=int(input())
s=n*n
k=int(math.log10(n)+1)
f=s%int(10**k)
if(f==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")