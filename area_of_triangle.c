a=float(input("Enter first side of triangle :"))
b=float(input("Enter second side of triangle :"))
c=float(input("Enter third side of triangle :"))
s=(a+b+c)/2
a=(s*(s-a)*(s-b)*(s-c))**(1/2)
print("Area of triangle is :%.2f"%a)
