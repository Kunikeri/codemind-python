n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,n):
    if i%2==0:
        s1+=l[i]
    else:
        s2+=l[i]
print(s1-s2)