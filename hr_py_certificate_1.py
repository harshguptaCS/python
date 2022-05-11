n=input()
s=n
n=n.lower()
l=n.split()
l2=s.split()
for i in range(len(l)):
    l[i]=list(l[i])
    l2[i]=list(l2[i])
    for j in range(1,len(l[i])):
        if(ord(l[i][j])>ord(l[i][j-1])):
            if(l2[i][j].islower()):
                l2[i][j]=chr(ord(l2[i][j])-32)
        elif(ord(l[i][j])<ord(l[i][j-1])):
            if(l2[i][j].isupper()):
                l2[i][j]=chr(ord(l2[i][j])+32)
    l2[i]=''.join(l2[i])        
l2=' '.join(l2)    
print(l2)
