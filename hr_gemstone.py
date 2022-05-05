n=int(input())
l=[]
for i in range(n):
    l.append(input())
ans=[]    
for i in l[0]:
    x=0
    for j in l:
        if(i in j):
            x+=1
        else:
            break
    if(x==n):
        ans.append(i)
print(len(set(ans)))                        
