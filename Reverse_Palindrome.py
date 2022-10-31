def gani(x):
    c=0
    while x>0:
        r=x%10
        c=c*10+r
        x=x//10
    return c
x=int(input())
while True:
    x=x+gani(x)
    if x==gani(x):
        print(x)
        break
    