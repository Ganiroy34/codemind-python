x=int(input())
s=x*x
c=0
while s>0:
    n=s%10
    s=s//10
    c=c+n
if x==c:
    print('Neon Number')
else:
    print('Not Neon Number')