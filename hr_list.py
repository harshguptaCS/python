n=int(input())
lst=[]
for i in range(0,n):
    l=[]
    l.extend(i for i in input().split())
    for j in range(1,len(l)):
        l[j]=int(l[j])
    if(l[0]=="insert"):
        lst.insert(l[1],l[2])
    elif(l[0]=="print"):
        print(lst)
    elif(l[0]=="remove"):
        lst.remove(l[1])
    elif(l[0]=="append"):
        lst.append(l[1])
    elif(l[0]=="sort"):
        lst.sort()
    elif(l[0]=="pop"):
        lst.pop()
    elif(l[0]=="reverse"):
        lst.reverse()
