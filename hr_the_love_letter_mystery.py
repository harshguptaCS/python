n=int(input())
ans=[]
for i in range(n):
    s=input()
    o=0
    for i in range(len(s)//2):
        o+=abs(ord(s[i])-ord(s[-1-i]))
    ans.append(o)
for i in ans:
    print(i)
