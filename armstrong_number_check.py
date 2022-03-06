n=int(input("Enter a number :"))
temp=l=n
x=s=0
while n>0:
    x=x+1
    n=n//10
while l>0:
    r=l%10
    s=s+r**x
    l=l//10
if s==temp:
    print("Armstrong")
else:
    print("Not Armstrong")
