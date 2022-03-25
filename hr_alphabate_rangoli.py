n=int(input())
for i in range(0,n-1):
    s=''
    for j in range(0,i+1):
        s=s+chr(96+n-j)+'-'
    for k in range(1,i+1):
        s=s+chr(96+n-j+k)+'-'    
    print(s.center(4*n-3,'-'))  
s=''    
for j in range(0,n):
    s=s+chr(96+n-j)+'-'
for k in range(1,n):
    s=s+chr(96+n-j+k)+'-'    
print(s[0:-1])    
for i in range(n-1,0,-1):
    s=''
    for j in range(0,i):
        s=s+chr(96+n-j)+'-'
    for k in range(1,i):
        s=s+chr(96+n-j+k)+'-'    
    print(s.center(4*n-3,'-'))        
