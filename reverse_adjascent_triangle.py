n=int(input())
print('*'*(2*n-1))
for i in range(n-1,0,-1):
    print(('*'*i).ljust(n-1),('*'*i).rjust(n-1))
