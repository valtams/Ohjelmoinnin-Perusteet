def main():
	print("Program starting.")
	word = input("Insert word: ")
	frameWord(word)
	print("\nProgram ending.")
	return None

def frameWord(PWord):
	l = len(PWord)
	print("*" * (l + 4))
	print(f"* {PWord} *")
	print("*" * (l + 4))
	return None

main()