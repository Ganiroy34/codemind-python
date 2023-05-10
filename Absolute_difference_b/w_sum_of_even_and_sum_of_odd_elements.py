n=int(input())
a=list(map(int,input().split()))
s=0
b=0
for i in range(n):
    if a[i]%2==0:
        s+=a[i]
    else:
        b+=a[i]
print(abs(b-s))
        