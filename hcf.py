a,b=(int(i) for i in input("Enter two numbers :").split())
m=a if a<b else b
while 1:
    if a%m==0 and b%m==0:
        h=m
        break
    m-=1   
print("HCF : ",h)    
