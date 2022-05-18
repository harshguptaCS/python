n=input()
s=input()
l=list(s)
x=0
for i in range(0,len(l)-2):
    if(l[i:i+3]==['0','1','0']):
        l[i+2]='1'
        x+=1
print(x)        
