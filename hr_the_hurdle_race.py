n,k=(int(i) for i in input().split())
l=list(map(int,input().split()))
m=max(l)
if(m>k):
    print(m-k)
else:
    print("0")    
