h,m,s=(i for i in input().split(":"))
if(s[2:]=="AM"):
    if(h=="12"):
        h="00"
if(s[2:]=="PM"):
    h=int(h)
    if(h!=12):
        h+=12
print(h,m,s[0:2],sep=':')    
