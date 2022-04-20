n,m=(int(i) for i in input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
m1=max(l1)
m2=min(l2)
x=0
for i in range(m1,m2+1):
    temp=1
    for j in l1:
        if(i%j!=0):
            temp=0
            break
    if(temp==1):
        for j in l2:
            if(j%i!=0):
                temp=0
                break
    if(temp==1):
        x+=1            
print(x)        
