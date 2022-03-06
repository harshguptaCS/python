n=int(input("Enter a number :"))
print("FACTORS : ",end='')
for i in range(1,int(n/2+1)):
    if n%i==0:
        print(i,end=" ")
