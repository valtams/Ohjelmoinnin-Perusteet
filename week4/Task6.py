print("Program starting.")
i = int(input("Insert a positive integer: "))
c = 0
if i <= 0:
	print("Only positive integers are allowed.")
while i != 1:
	c += 1
	print(i, end=" -> ")
	if i % 2 == 1:
		i = i * 3 + 1
	else: i //= 2
print(i)
print(f"Sequence {c} total steps.")
print("\nProgram ending.")
