x=int(input())
s=0
r=x
if x>0:
    while x>0:
        n=x%10
        s=s*10+n
        x=x//10
else :
    x=-x
    while x>0:
        
        n=x%10
        s=s*10+n
        x=x//10
if r>0:
    print(s)
else:
    print(-s)