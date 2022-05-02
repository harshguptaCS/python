n=int(input())
l=list(map(int,input().split()))
i=x=0
while(1):
    if(i==n-1):
        break
    if(i<n-2 and l[i+2]==0):
        x+=1
        i=i+2
    elif(l[i+1]==0):
        x+=1    
        i=i+1
    else:
        break
print(x)        
