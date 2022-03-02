a,b,c=(int(i) for i in input("Enter three variable :").split())
M=max(a,b,c)
m=min(a,b,c)
m2=a+b+c-M-m
print("Variables in decreasing order",M,m2,m)
