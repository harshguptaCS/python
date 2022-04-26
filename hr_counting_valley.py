n=int(input())
s=input()
x=a=0
for i in range(0,len(s)):
    if(s[i]=='U'):
        x-=1
    else:
        x+=1
    if(x==0 and s[i]=='U'):
        a+=1
print(a)                
