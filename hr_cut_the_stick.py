n=int(input())
lst=list(map(int,input().split()))
for i in range(0,n):
    m=max(lst)
    for j in range(0,n):
        if(m>lst[j] and lst[j]!=0):
            m=lst[j]
    x=0
    for j in range(0,n):
        if(lst[j]>0):
            lst[j]=lst[j]-m
            x+=1
    if(x>0):
        print(x)    
