for i in range(3, 31, 2):
	output = "#"*i
	print(output)
	print("".join(" " if j % 2 == 1 else char for j, char in enumerate(output)))
print(output)