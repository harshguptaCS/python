import random
a,b=(int(i) for i in input("Enter range for random number :").split())
x= random.randint(a,b)
print("Random Number :",x)
