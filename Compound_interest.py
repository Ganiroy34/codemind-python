p,r,t=map(int,input().split())
c=pow(1+r/100,t)
d=p*c
print('%.2f'%d)