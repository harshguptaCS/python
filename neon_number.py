n=int(input("Enter a number : "))
x=n**2
s=0
while x>0:
    r=x%10
    s+=r
    x=x//10
if n==s:
    print("Neon Number")
else :
    print("Not Neon Number")
