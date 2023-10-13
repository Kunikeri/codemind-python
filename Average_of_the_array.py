n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s+=i
a=s/n
print('%.2f'%a)