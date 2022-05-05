n=int(input())
l=[]
for i in range(n):
    s1=input()
    s2=input()
    l.append(len(set(s1))+len(set(s2))!=len(set(s1+s2)))
for i in l:
    if(i):
        print("YES")
    else:
        print("NO")
