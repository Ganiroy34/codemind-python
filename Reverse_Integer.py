a=int(input())
s=0
f=0
if (a<0):
    a=abs(a)
    f=1
while(a>0):
    g=a%10
    s=g+s*10
    a=a//10
    
if(f==1):
    print(-1*s)
else:print(s)    