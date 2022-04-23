a,b=(int(i) for i in input("Enter two numbers : ").split())
z=a^b
z=bin(z)
x=str(z)
y=0
for i in range(2,len(x)):
    if x[i]=='1':
        y+=1
print("Hamming distance =",y)
