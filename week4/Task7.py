def per(n):
	if len(str(n)) == 1:
		print("No more steps.")
		return
	digits = [int(i) for i in str(n)]

	result = 1
	for j in digits:
		result *= j
	print(f'{" * ".join(str(n))} = {result}')
	per(result)

print("Program starting.\n")
print("Check multiplicative persistence.")
n = int(input("Insert an integer: "))
per(n)