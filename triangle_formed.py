a,b,c=(int(i) for i in input("Enter three sides :").split())
if a+b>c and a+c>b and b+c>a :
    print("Triangle can formed")
else :
    print("Triangle can not formed")
