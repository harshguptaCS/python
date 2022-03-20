s=input()
a=s[0]
x=0
for i in range(0,len(s)):
    if s[i]==a:
        x+=1
    else:
        print("(%d, %s)"%(x,a),end=' ')
        a=s[i]
        x=1
print("(%d, %s)"%(x,a),end=' ')
