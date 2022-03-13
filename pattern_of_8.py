n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==1 or j==1 or i==n or j==n) and (i!=j and i+j!=n+1):
            print("*",end="")
        else :
            print(" ",end="")
    print()    
for i in range(2,n+1):        
    for j in range(1,n+1):
        if (j==1 or j==n or i==n)and (i!=j and i+j!=n+1):
            print("*",end="")
        else :
            print(" ",end="")
    print()
