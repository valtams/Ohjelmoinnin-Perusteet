def menuOptions():
	print("Options:")
	print("1 - In one multi-branched decision")
	print("2 - In multiple independednt if-statements")
	print("0 - Exit")

print("Program starting.")
print("Testing decision structures")
I = int(input("Insert an integer: "))
menuOptions()
Choice = int(input("Your choice: "))
if Choice == 0:
	print("Exiting...")
elif Choice == 1:
	if I >= 400:
		I += 44
	elif I >= 200:
		I += 22
	elif I >= 100:
		I += 11
	else: I += 0
	print(f"The result is {I}")
elif Choice == 2:
	if I >= 400:
		I += 44
	if I >= 200:
		I += 22
	if I >= 100:
		I += 11
	print(f"The result is {I}")
else:
	print("Unknown option.")

print("\nProgram ending.")