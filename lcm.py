a,b=(int(i) for i in input("Enter two numbers :").split())
m=a if a>b else b
while 1:
    if m%a==0 and m%b==0:
        l=m
        break
    m+=1   
print("LCM : ",l)    
