l=int(input())
n=int(input())
while n:
    w,h=map(int,input().split())
    if l>h or l>w:
        print('UPLOAD ANOTHER')
    elif h==w:
        print ('ACCEPTED')
    else:
         print('CROP IT')
n-=1         
         