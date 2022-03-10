n,m=[int(i) for i in input("Enter the range :").split()]
for i in range(n,m+1):
    temp=l=i
    x=s=0
    while temp>0:
        x=x+1
        temp=temp//10
    while l>0:
        r=l%10
        s=s+r**x
        l=l//10
    if s==i:
        print(s,end=' ')
