print("Calculate the area of a wall.")
Width = input("Enter the width in meters: ").replace(",",".")
Height = input("Enter the height in meters: ").replace(",",".")
Area = float(Width) * float(Height)
print(f"Width is {Width} m and height is {Height} m.")
if Area % 1 == 0:
        Area = int(Area)
else: Area = round(Area, 2)
print(f"The wall will be {Area} square meters.")