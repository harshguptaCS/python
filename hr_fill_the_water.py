t=int(input())
v=15*t
if v==785:
    print("The water tank is full, turn off the pump. Thank you")
elif v>785:
    print("Overflow\n%.1f"%(v-785))
else:
    print("Underflow")
    h=v/78.5
    print("%.2f\n%.2f"%(h,10-h))
