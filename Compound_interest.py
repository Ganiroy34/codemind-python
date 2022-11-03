p,r,t=map(int,input().split())
c=pow(1+r/100,t)
n=(p*c)
print('%.2f'%n)
