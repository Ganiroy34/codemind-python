a=int(input())
b=int(input())
def selfd(n):
    num=n
    if n<10:
        return True
    while n>0:
        r= n%10 
        if r==0:
            return False
        if num%r!=0:
            return False
        n=n//10
    return True
for i in range(a,b+1):
    if selfd(i):
        print(i,end=' ')
            