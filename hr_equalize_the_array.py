n=int(input())
l=list(map(int,input().split()))
l.sort()
x=1
ans=[]
a=l[0]
for i in range(1,len(l)):
    if(l[i]==a):
        x+=1
    else:
        ans.append(x)
        a=l[i]
        x=1
ans.append(x)
print(n-max(ans))        
