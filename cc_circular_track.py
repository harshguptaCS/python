t=int(input())
for i in range(t):
    a,b,m=(int(i) for i in input().split())
    x=abs(b-a)
    y=m-b+a
    z=m-a+b
    print(min(x,y,z))   
