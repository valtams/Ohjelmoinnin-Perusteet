print("Calculate fuel consumption.")
Feed = input("Enter travel distance (Include units): ")
Units = Feed[-2:]
Distance = int(Feed.replace(Units,""))
if Units == "mi":
	Usage = int(input("Enter fuel usage (gallons): "))
	Consumption = Distance / Usage
	print(f"Fuel consumption is {round(Consumption, 2)}mpg")
elif Units == "km":
	Usage = int(input("Enter fuel usage (liters): "))
	Consumption = Usage / (Distance / 100)
	print(f"Fuel consumption is {round(Consumption, 2)}l/100km")
else: print("Only l/100km and mpg are supported")
