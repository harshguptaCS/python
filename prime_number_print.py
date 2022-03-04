n=int(input("Enter lower range :"))
m=int(input("Enter upper range :"))
for j in range(n,m+1):
    fl=0
    if n>1:
        for i in range(2,int(j/2)+1):
            if j%i==0:
                fl=1
                break
    else:
        fl=1
    if fl==0:
        print(j,end=' ')
