n=int(input("Enter a number : "))
temp=n
l=n%10
x=-1
while temp>0:
    x+=1
    f=temp%10
    temp=temp//10
nn= (n-f*10**x)+l*10**x-l+f
print("New number :",nn)
