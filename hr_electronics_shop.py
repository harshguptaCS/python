b,n,m=(int(i) for i in input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
x=-1
for i in range(n):
    for j in range(m):
        if(l1[i]+l2[j]<=b and l1[i]+l2[j]>x):
            x=l1[i]+l2[j]
print(x)            
