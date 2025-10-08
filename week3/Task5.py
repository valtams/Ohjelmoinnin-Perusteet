def menuOptions():
	print("\n")
	print("Options:")
	print("1 - Celsius to Fahrenheit")
	print("2 - Fahrenheit to Celsius")
	print("0 - Exit")

def CtoF():
	c = float(input("Insert Celsius: "))
	print(f"{c} °C is {round((c * 9/5) + 32, 1)} °F")

def FtoC():
	f = float(input("Insert Fahrenheit: "))
	print(f"{f} °F is {round((f - 32) * 5/9, 1)} °C")

print("Program starting.")
print("This is a program with simple menu where you can choose which operation the program performs")
Name = input("Before the menu, please insert your name: ")
menuOptions()
Choice = int(input("Your choice: "))
if Choice == 0:
	print("Exiting...")
elif Choice == 1:
	CtoF()
elif Choice == 2:
	FtoC()
else:
	print("Unknown option.")
print("\nProgram ending.")