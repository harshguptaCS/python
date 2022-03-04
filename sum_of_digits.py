n=n=int(input("Enter a number :"))
temp=n
ans=0
while(temp!=0):
    ans+=temp%10
    temp=temp//10
print("Sum of its digits =",ans)    
