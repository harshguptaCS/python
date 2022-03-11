pas=input()
a=b=c=d=0
for i in range(0,len(pas)):
    if 'a'<=pas[i] and pas[i]<='z':
        a=1
    elif 'A'<=pas[i] and pas[i]<='Z':    
        b=1
    elif '0'<=pas[i] and pas[i]<='9':    
        c=1
    else:
        d=1
x=4-(a+b+c+d)
y=6-len(pas)
ans = x if x>y else y
print(ans)
