l=list(map(int,input().split()))
s=input()
l2=len(s)
s=list(set(s))
h=1
for i in s:
    if(l[ord(i)-97]>h):
        h=l[ord(i)-97]
print(h*l2)        
