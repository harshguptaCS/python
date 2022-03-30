lst=[]
s=0
lst.extend(int(i) for i in input("Enter list element :").split())
for i in lst:
    if i<0:
        s+=i
print("Sum of negative numbers :",s)        
