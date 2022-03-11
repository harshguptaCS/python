n=int(input("Enter a number : "))
for i in range(0,n):
    print("  "*(i),"*"*(n-i))
for i in range(n-1,-1,-1):
    print("  "*(i),"*"*(n-i))    
