print("Program starting.")
print("Estimate how many minutes you spent on programming...")
Task1 = int(input("Task 1: "))
Task2 = int(input("Task 2: "))
Task3 = int(input("Task 3: "))
Task4 = int(input("Task 4: "))
Task5 = int(input("Task 5: "))
Task6 = int(input("Task 6: "))
Task7 = int(input("Task 7: "))
Total = Task1 + Task2 + Task3 + Task4 + Task5 + Task6 + Task7
#Total = 23 
Seconds = (Total * 60 / 7) % 60
print(f"In total you spent {Total} minutes on programming.")
print(f"Average per task was {Total//7} minutes and {Seconds:.0f} seconds or roughly {round(Total / 7)} minutes.")
print("Program ending.")