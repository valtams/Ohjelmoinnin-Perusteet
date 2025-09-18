print("Program starting.\n")
Input = input("Insert a hex color: ").replace("#", "")
if len(Input) == 3 or len(Input) == 6:
	if len(Input) == 3:
		Input = Input[0]*2 + Input[1]*2 + Input[2]*2
	R = Input[0:2]
	G = Input[2:4]
	B = Input[4:6]
	print(f"\nColors\n- Red {R}\n- Green {G}\n- Blue {B}\n")
else: print("Invalid hex color.")
print("Program ending.")