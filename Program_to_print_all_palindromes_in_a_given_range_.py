a=int(input())
b=int(input())
l=[]
for i in range(a,b):
    x=i
    s=0
    
    while x>0:
        r=x%10
        s=s*10+r
        x=x//10
    if s==i:
        print(s,end=" ") 