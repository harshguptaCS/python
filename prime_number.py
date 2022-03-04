n=int(input("Enter a number :"))
fl=0
if n>1:
    for i in range(2,int(n/2)+1):
        if n%i==0:
            fl=1
            break
else:
    fl=1
if fl==0:
    print("Prime Number")
else:
    print("Not Prime Number")
