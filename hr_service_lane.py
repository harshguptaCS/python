n,k=(int(i) for i in input().split())
l=list(map(int,input().split()))
t=[]
for i in range(k):
    a,b=(int(i) for i in input().split())
    t.append([a,b])
for i in t:
    print(min(l[i[0]:i[1]+1]))    
