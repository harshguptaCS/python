lst1=[]
lst2=[]
s=0
lst1.extend(eval(i) for i in input("Enter first list element :").split())
lst2.extend(eval(i) for i in input("Enter second list element :").split())
lst1[0],lst2[0]=lst2[0],lst1[0]
print("First list :",lst1)
print("Second list :",lst2)
