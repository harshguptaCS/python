s=input()
for i in range(0,len(s)):
    if i%2==0: print(s[i].upper(),end='')
    else : print(s[i].lower(),end='')
