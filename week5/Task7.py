DELIMITER = ","

def main():
	words = collectWords()
	analyseWords(words)

def collectWords():
	words = []
	while True:
		word = input("Insert a word(empty stops): ")
		if word == "":
			break
		words.append(word)
	return DELIMITER.join(words)

def analyseWords(w):
	print(f"- {len(w.split(DELIMITER))} Words")
	print(f"- {len(w) - w.count(DELIMITER)} Characters")
	Avg = (len(w) - w.count(DELIMITER)) / len(w.split(DELIMITER))
	print("- {:.2f} Average word length".format(Avg))

print("Program starting.")
main()
print("Program ending.")