y=int(input("Enetr the year :"))
if (y%4==0 and y%100!=0) or y%400==0:
    print("Leap year")
else:
    print("NOT Leap year")
