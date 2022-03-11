a,b=(int(i) for i in input("Enter two numbers : ").split())
for i in range(a,-b-1,-1):
    if i%b==0 and i!=0:
        print(abs(i))
        break
