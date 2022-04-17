n,k=(int(i) for i in input().split())
l=list(map(int,input().split()))
x=0
p=1
for i in range(n):
    for j in range(1,l[i]+1):
        fl=0
        if(j==p):
            x+=1
        if(j%k==0):
            fl=1
            p+=1
    if(fl==0):
        p+=1
print(x)        
