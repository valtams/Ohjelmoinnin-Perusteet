print("Program starting.\n")
word = input("Insert a word: ")
words = 0
sentence = ""
while word != "":
	words += 1
	sentence += word + " "
	word = input("Insert a word: ")
print(f"\nYou inserted:\n- {words} words\n- {len(sentence)- words} characters")