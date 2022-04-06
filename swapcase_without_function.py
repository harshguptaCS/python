s=input()
s2=''
for i in range(0,len(s)):
    if('a'<=s[i]<='z'):
        s2+=chr(ord(s[i])-32)
    elif('A'<=s[i]<='Z'):
        s2+=chr(ord(s[i])+32)
    else:
        s2+=s[i]
print(s2)        
