n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in l:
    if i%2==0:
        s1+=i
for i in l:
    if i%2!=0:
        s2+=i
print(abs(s2-s1))