n,k=(int(i) for i in input().split())
l=list(map(int,input().split()))
i=x=0
l2=[]
while((i+k)%n!=0):
    l2.append(l[i%n])
    i+=k
    x+=1
x+=1    
l2.append(l[i%n])
for i in l2:
    if(i==1):
        x+=2
if(100-x>0):
    print(100-x)
else:
    print("0")                
