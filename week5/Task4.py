def askDimension(PPrompt: str) -> float:
   Feed = input(f"Insert {PPrompt}: ")
   return float(Feed)

Width = askDimension("width")
Height = askDimension("height")

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
   Area = PWidth * PHeight
   return Area

Area = calcRectangleArea(Width, Height)
print("Program starting.")
print(f"Area is {Area:.1f}²")
print("Program ending.")