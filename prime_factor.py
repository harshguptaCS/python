n=int(input("Enter a number : "))
print("prime factor :",end='')
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            print(i,end=' ')
            n=n//i
            break
