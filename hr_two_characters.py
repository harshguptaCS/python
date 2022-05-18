n=int(input())
s=input()
l=list(s)
se=list(set(s))
x=[]
for i in range(0,len(se)-1):
    for j in range(i+1,len(se)):
        l1=[]
        for k in l:
            if(k==se[i] or k==se[j]):
                l1.append(k)
        s1=set(l1[0::2])
        s2=set(l1[1::2])
        if(len(s1)==1 and len(s2)==1):
            x.append(len(l1))
if len(x)>0:            
    print(max(x))            
else:
    print("0")    
