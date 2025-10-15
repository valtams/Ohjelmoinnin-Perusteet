def main():
	while True:
		options()
		choice = int(input("Your choice: "))
		if choice == 0:
			print("\nProgram ending.")
			break
		elif choice == 1:
			word = input("Insert word: ")
		elif choice == 2:
			try:
				print(f'Current word - "{word}"')
			except NameError:
				print("No word inserted yet.")
		elif choice == 3:
			try:
				print(f'Word reversed - "{word[::-1]}"')
			except NameError:
				print("No word inserted yet.")
		else: print("Unknown option.")

def options():
	print("Options:")
	print("1 - Insert word")
	print("2 - Show current word")
	print("3 - Show current word in reverse")
	print("0 - Exit")
	return None

print("Program starting.")
main()