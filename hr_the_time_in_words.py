l=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","tweleve","one"]
l2=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","tweleve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","ninteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty"]
h=int(input())
m=int(input())
if(m==0):
    print(l[h-1],"o' clock")
elif(m<30):
    if(m==15):
        print("quarter past",l[h-1])
    elif(m==1):
        print("one minute past",l[h-1])
    else:
        print(l2[m-1],"minutes past",l[h-1])
elif(m==30):
    print("half past",l[h-1])
else:
    if(m==45):
        print("quarter to",l[h])
    elif(m==59):
        print("one minute to",l[h])
    else:
        print(l2[60-m-1],"minutes to",l[h])
