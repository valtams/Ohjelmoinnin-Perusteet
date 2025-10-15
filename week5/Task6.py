def main():
	count = 0
	while True:
		showOptions()
		choice = askChoice()
		if choice == 0:
			print("Exiting program.")
			break
		elif choice == 1:
			print(f'Current count - {count}\n')
		elif choice == 2:
			count += 1
			print('Count increased!\n')
		elif choice == 3:
			count = 0
			print("Cleared count!\n")
		else: 
			print("Unknown option!\n")

def showOptions():
	print("Options:")
	print("1 - Show count")
	print("2 - Increase count")
	print("3 - Reset count")
	print("0 - Exit")
	return None

def askChoice():
	choice = input("Your choice: ")
	if not choice.isnumeric():
		choice = -1
	return int(choice)

print("Program starting.")
main()
print("\nProgram ending.")