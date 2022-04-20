y=int(input())
if(y<1918):
    if(y%4==0):
        print("12.09",y,sep='.')
    else:
        print("13.09",y,sep='.')
elif(y>1918):
    if(y%4==0 and y%100!=0) or y%400==0:
        print("12.09",y,sep='.')
    else:
        print("13.09",y,sep='.')
else:
    print("26.09",y,sep='.')        
