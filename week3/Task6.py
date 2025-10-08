def menuOptions():
	print("\n")
	print("Options:")
	print("1 - Length")
	print("2 - Weight")
	print("0 - Exit")

def LengthMenu():
	print("\n")
	print("Length options:")
	print("1 - Meters to kilometers")
	print("2 - Kilometers to meters")
	print("0 - Exit")
	Choice = input("Your choice: ")

	if Choice == "0": print("Exiting...")
	elif Choice == "1":
		m = float(input("Insert meters: "))
		print(f"{m} m is {round(m / 1000, 1)} km")
	elif Choice == "2":
		km = float(input("Insert kilometers: "))
		print(f"{km} km is {round(km * 1000, 1)} m")
	else: print("Unknown option.")

def WeightMenu():
	print("\n")
	print("Weight options:")
	print("1 - Grams to pounds")
	print("2 - Pounds to grams")
	print("0 - Exit")
	Choice = input("Your choice: ")

	if Choice == "0": print("Exiting...")
	elif Choice == "1":
		g = float(input("Insert grams: "))
		print(f"{g} g is {round(g * 0.002205, 1)} lb")
	elif Choice == "2":
		lb = float(input("Insert pounds: "))
		print(f"{lb} lb is {round(lb * 453.6, 1)} g")
	else: print("Unknown option.")

print("Program starting.\nWelcome to the unit converter program!\nFollow the menu instructions below.")
menuOptions()
Choice = int(input("Your choice: "))
if Choice == 0: print ("Exiting...")
elif Choice == 1:
    LengthMenu()
elif Choice == 2:
    WeightMenu()
else: print("Unknown option.")
print("\nProgram ending.")
