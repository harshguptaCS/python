n=int(input())
l1=[]
l2=[]
for i in range(0,n):
    l1.append(input())
    l2.append(eval(input()))
m=min(l2)
m2=max(l2)
for i in range(0,n):
    if(m2>l2[i] and l2[i]>m):
        m2=l2[i]
l3=[]        
for i in range(0,n):
    if(l2[i]==m2):
        l3.append(l1[i])
l3.sort()
for i in l3:
    print(i)
