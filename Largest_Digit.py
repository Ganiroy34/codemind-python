n=int(input())
s=0
while n>0:
    r=n%10
    n=n//10
    if s<r:
        s=r
print(s)