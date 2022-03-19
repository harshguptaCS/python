s=input()
i=0
while i<len(s)-1:
    if s[i]==s[i+1]:
        s=s.replace(s[i:i+2],'')
        i=0
    else:
        i+=1
if s!='':        
    print(s)     
else:
    print('Empty String')
