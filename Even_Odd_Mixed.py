a=int(input())
s=0
t=0
while a>0:
    r=a%2==0
    a=a//10
    if r%2==0:
        s+=1
    else:
        t+=1
if s>0 and t>0:
    print('Mixed')
elif s>0 and t==0:
    print('Odd')
else:
    print('Even')
    
    
    
    
