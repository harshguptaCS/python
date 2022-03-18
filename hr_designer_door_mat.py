m,n=(int(i) for i in input().split())
for i in range(m//2):
    print((".|."*(2*i+1)).center(n,"-"))
print("WELCOME".center(n,'-'))    
for i in range(m//2,0,-1):
    print((".|."*(2*i-1)).center(n,"-"))
