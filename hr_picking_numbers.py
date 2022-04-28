n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n):
    x=0
    for j in range(n):
        if l[j]==l[i] or l[j]==l[i]+1:
            x+=1
    a.append(x)
print(max(a))            
