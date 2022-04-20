n=int(input())
l=list(map(int,input().split()))
d,m=(int(i) for i in input().split())
x=0
for i in range(0,n-m+1):
    s=0
    for j in range(i,i+m):
        s+=l[j]
    if(s==d):
        x+=1
print(x)            
