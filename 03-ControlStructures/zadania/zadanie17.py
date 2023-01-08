x=int(input("type your x coordinate: "))
y=int(input("type your y coordinate: "))

print(f"Point ({x},{y}) is in the ")
if x>0:
    if y>0:
        print("first")
    else:
        print("fourth")
else:
    if y<0:
        print("third")
    else:
        print("second" )

print("quadrant of the coordinate system")
