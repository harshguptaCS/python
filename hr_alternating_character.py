t=int(input())
for i in range(t):
    s=input()
    a=s[0]
    x=0
    for j in range(1,len(s)):
        if(a==s[j]):
            x+=1
        else:
            a=s[j]
    print(x)            
