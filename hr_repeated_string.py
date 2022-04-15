s=input()
n=int(input())
x=y=0
for i in range(len(s)):
    if(s[i]=='a'):
        x+=1
if n%len(s)!=0:
    for j in range(0,n%len(s)):
        if(s[j]=='a'):
            y+=1            
r=(n//len(s))*x+y
print(r)            
