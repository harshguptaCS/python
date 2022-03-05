n=int(input("Enter a number :"))
temp=n
ans=0
while(temp!=0):
    r=temp%10
    ans=10*ans+r
    temp=temp//10
print("Reverse =",ans)    
