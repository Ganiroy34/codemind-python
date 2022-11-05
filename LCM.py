a,b=map(int,input().split())
if a>b:
    max=(a)
else:
    max=(b)
while max>1:
    if (max%a==0 and max%b==0):
        break
    max+=1
print(max)    
