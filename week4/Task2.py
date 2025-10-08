print("Program starting.\n")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
output = ""
print("\nStarting for-loop:")
for i in range(start, stop):
	print(i, end=" ")
print(i + 1)
#for i in range(start, stop +1):
#	output += str(i) + " "
#print(output[:-1])
print("\nProgram ending.")