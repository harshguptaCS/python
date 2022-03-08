n=int(input("Enter a number : "))
temp=n
n2=0
while temp>0:
    r=temp%10
    n2=10*n2+r
    temp=temp//10 
while n2>0:
    f=n2%10
    n2=n2//10
    if f==0: print("zero",end=' ')
    elif f==1: print("one",end=' ')
    elif f==2: print("two",end=' ')
    elif f==3: print("three",end=' ')
    elif f==4: print("four",end=' ')
    elif f==5: print("five",end=' ')
    elif f==6: print("six",end=' ')
    elif f==7: print("seven",end=' ')
    elif f==8: print("eight",end=' ')
    else: print("nine",end=' ')
