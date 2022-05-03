n=int(input())
l=list(map(int,input().split()))
d=[]
fl=0
for i in range(n-1):
    for j in range(i+1,n):
        if(l[i]==l[j]):
            d.append(j-i)
            fl=1
            break
if(fl==1):
    print(min(d))        
else:
    print("-1")
