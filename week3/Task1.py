print("Program starting.")
print("Insert two integers.")
a = int(input("Insert first integer: "))
b = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if a < b:
    print("Second integer is greater than first integer")	
elif a > b:
    print("First integer is greater than second integer")
else:
    print("Integers are the same")
print("\nAdding integers together")
sum_ab = a + b
print(f"{a} + {b} = {sum_ab}")
print("\nChecking the parity of the sum...")
if sum_ab % 2 == 0:
    print("Sum is even.")
    
print("Program ending.")