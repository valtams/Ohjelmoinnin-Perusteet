def askDimension(PPrompt: str) -> float:
   Feed = float(input(f"Insert {PPrompt}: "))
   return Feed

Width = askDimension("width")
Height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Sum = PWidth * PHeight
   return Sum

Area = calcRectangleArea(Width, Height)
print("Program starting.")
print(f"Area is {Area:.1f}²")
print("Program ending.")