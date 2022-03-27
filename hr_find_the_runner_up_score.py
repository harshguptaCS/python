n=int(input())
l=[]
l= list(map(int,input().strip().split()))[:n]
m=max(l)
x=min(l)
for i in range(0,n):
    if(x<l[i] and l[i]!=m):
        x=l[i]
print(x)        
