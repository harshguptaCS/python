t=int(input())
for j in range(t):
    n,k=(int(i) for i in input().split())
    l=list(map(int,input().split()))
    m=0
    for i in l:
        if(i<=0):
            m+=1
    if(m<k):
        print("YES")
    else:
        print("NO")    
