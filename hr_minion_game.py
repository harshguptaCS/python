s=input()
x=y=0
for i in range(0,len(s)):
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
        x+=len(s)-i
    else:
        y+=len(s)-i
if x>y:
    print("Kevin",x)
elif y>x:
    print("Stuart",y)
else:
    print("Draw")
