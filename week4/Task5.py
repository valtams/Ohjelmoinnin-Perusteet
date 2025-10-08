print("Program starting.\n")
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: ")) 
inspect = int(input("Insert inspection point: "))
output = []
if start >= stop:
	print("Starting point value must be less than the stopping point value.")
if inspect < start or inspect > stop:
	print("Inspection value must be within the range of start and stop.")
print("\nFirst loop - inspection with break:")
for i in range(start, stop - 1):
	if i == inspect:
		break
	else: output.append(str(i))
print(" ".join(output))
print("Second loop - inspection with continue:")
for i in range(start, stop - 1):
	if i == inspect:
		continue
	else: print(i, end=" ")
print(i + 1)
print("\nProgram ending.")