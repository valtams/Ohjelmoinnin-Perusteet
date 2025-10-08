print("Program starting.\n")
print("Check multiplicative persistence.")
#n = number, c = count, d = digits, r = result
n = int(input("Insert an integer: "))
c = 0
while len(str(n)) > 1:
	c += 1
	d = [int(i) for i in str(n)]
	r = 1
	for j in d:
		r *= j
	print(f'{" * ".join(str(n))} = {r}')
	n = r
print("No more steps.")
print(f"\nThis program took {c} step(s)")
print("\nProgram ending.")