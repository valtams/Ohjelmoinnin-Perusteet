def main():
	print("Program starting.")
	greetUser(askName())
	print("Program ending.")
	return None

def askName():
	name = input("Insert name: ")
	return name

def greetUser(PName):
	print(f"Hello {PName}!")
	return None

main()