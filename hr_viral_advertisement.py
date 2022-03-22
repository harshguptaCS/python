n=int(input())
p=5
s=0
for i in range(1,n+1):
    k=p//2
    p=k*3
    s=s+k
print(s)    
