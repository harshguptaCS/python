n=int(input("Enter a number : "))
temp=n
s=0
while temp>0:
    r=temp%10
    f=1
    temp=temp//10
    for i in range(1,r+1):
        f=f*i
    s+=f
if s==n:
    print("strong number")
else:
    print("Not strong number")
