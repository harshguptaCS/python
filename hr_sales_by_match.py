n=int(input())
l=list(map(int,input().split()))
l.sort()
a=l[0]
x=s=0
for i in range(n):
    if(l[i]==a):
        x+=1
    else:
        a=l[i]
        s+=x//2
        x=1
s+=x//2        
print(s)        
