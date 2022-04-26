n=int(input())
p=int(input())
if(n%2==0):
    n+=1
if(n//2>=p):
    print(p//2)
else:
    print((n-p)//2)    
