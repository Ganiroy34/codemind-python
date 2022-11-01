def gani(a,b):
    c=6*b
    d=(30*a)+(0.5*b)
    f=abs(c-d)
    if f>180:
        return 360-f
    else:
        return f
        
        
        
        
y,h=map(int,input().split(":"))
print(gani(y,h))
    