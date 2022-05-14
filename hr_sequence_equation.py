n=int(input())
l=list(map(int,input().split()))
ans=l.copy()
for i in l:
    ans[l[l[i-1]-1]-1]=i
for i in ans:
    print(i)    
