n=int(input("Enter a number :"))
temp=n
l=n%10
ans=0
while(temp!=0):
    r=temp%10
    temp=temp//10
print("Sum of first and last digit :",(r+l))
