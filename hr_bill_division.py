n,k=(int(i) for i in input().split())
l=list(map(int,input().split()))
o=int(input())
s=0
for i in range(0,n):
    if(i==k):
        continue
    s+=l[i]
s=s//2
if(o>s):
    print(o-s)
else:
    print("Bon Appetit")     
