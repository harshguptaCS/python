t=int(input())
l=[]
for i in range(t):
    b,w=(int(i) for i in input().split())
    bc,wc,z=(int(i) for i in input().split())
    if(bc+z<wc):
        c=b*bc+w*(bc+z)
    elif(wc+z<bc):
        c=w*wc+b*(wc+z)
    else:
        c=b*bc+w*wc
    l.append(c)
for i in range(t):
    print(l[i])        
