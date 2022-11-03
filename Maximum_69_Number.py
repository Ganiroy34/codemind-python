def gani(a):
    g=list(str(a))
    e=g.count('6')
    if e>0:
        for i in range(0,len(g)):
            if g[i]=='6':
               g[i]='9'
               break
        return g
    elif e==0:
        return g
t=int(input())
g=gani(t)
for j in g:
    print(j,end='')