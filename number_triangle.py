n=int(input())
x=0
for i in range(1,n+1):
    for j in range(1,i+1):
        x+=1
        if x>9 : x=1
        print(x,end='')
    print()    
