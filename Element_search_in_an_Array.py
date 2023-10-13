n=int(input())
a=list(map(int,input().split()))
m=int(input())
f=0
for i in range(n):
    if a[i]==m:
        f=1
        break
if(f==1):
        print("True")
else:
        print("False")