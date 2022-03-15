s=input("Enter a string : ")
x=y=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        x+=1
    else:
        y+=1
print("Vowels =",x)
print("Consonant =",y)
