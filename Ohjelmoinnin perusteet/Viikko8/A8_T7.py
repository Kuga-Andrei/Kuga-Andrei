# A8_T7 Bestagons
# https://en.wikipedia.org/wiki/Hexagon

# Create menu-driven Python program, which can create squares, circles and hexagons. Focus of this assignment is in the creation of regular hexagons.

# Start the process of creating hexagon by prompting the user to set the center point. In SVGs, points are calculated from the top left corner.



# After center point has been collected, prompt the user again to insert apothem length. Use the apothem length to calculate the circumradius. Then calculate each hexagon corner point. Example solution calculates corners using math library’s .cos, .sin and .radians member functions. Start defining points from the top right corner point and move clockwise.

# Points to draw in order:

# Top Right
# Right
# Bottom Right
# Bottom Left
# Left
# Top Left


# Math terminology and formulas:

# : apothem or inradius (minimal radius)
# : circumradius (maximal radius)
# : side length

# See more details: https://www.gigacalculator.com/calculators/hexagon-calculator.php

# Polygon:

# The recommended svgwrite tool to create this shape is Polygon. Before applying points to the polygon shape, round the values into integers round(Value).

# Example points for hexagon with 60 inradius and center point (75, 75):

# Points = [
#     (109, 15),  # 109.64, 15.0
#     (144, 75),  # 144.28, 75.0
#     (110, 135), # 109.64, 135.0
#     (40, 135),  # 40.36, 135.0
#     (6, 75),    # 5.72, 75.0
#     (40, 15)    # 40.36, 15.0
# ]
# Apply also fill and stroke colors to the shape.

from drawLib import drawCircle, drawSquare, saveSvg, drawPolygon, Drawing

def main() -> None:
    # Initialize the drawing object
    Dwg = Drawing()
    print("Program starting.")
    while True:
        showOptions()
        choice = askChoice()
        match choice:
            case 1:
                print('Insert square')
                left = askValue1("Left edge position")
                top = askValue1("Top edge position")
                side = askValue1("Side length")
                color = askValue1("Fill color")
                stroke = askValue1("Stroke color")
                drawSquare(Dwg, left, top, side, color, stroke)
            case 2:
                print('Insert circle')
                x = askValue1("Center X coord")
                y = askValue1("Center Y coord")
                radius = askValue1("Radius")
                color = askValue1("Fill color")
                stroke = askValue1("Stroke color")
                drawCircle(Dwg, x, y, radius, color, stroke)
            case 4:
                filename = askValue2("Filename")
                print(f'Saving to file "{filename}"')
                proceed = askValue2("Proceed (y/n)?")
                if proceed.lower() == 'y':
                    saveSvg(Dwg, filename)
                    print("Vector saved successfully!")
                else:
                    print("Save cancelled.")

            case 3:
                print('Insert hexagon details:')
                centerX = askValue1("Middle point X")
                centerY = askValue1("Middle point Y")
                apothem = askValue1("Apothem length")
                color = askValue1("Insert fill")
                stroke = askValue1("Insert stroke")
                points = calcHexagonPoints(int(centerX), int(centerY), int(apothem))
                drawPolygon(Dwg, points, color, stroke)
  
            case 0:
                print("Exiting program.\n")
                break
            case _:
                print("Unknown option.\n")
        print()
    print("Program ending.")

def showOptions() -> None:
    print("Options:")
    print("1 - Draw square")
    print("2 - Draw circle") 
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def calcHexagonPoints(centerX: int, centerY: int, apothem: int) -> list:
    import math
    circumradius = apothem / math.cos(math.radians(30))
    points = []
    for angle in range(-60, 300, 60):
        rad = math.radians(angle)
        x = round(centerX + circumradius * math.cos(rad))
        y = round(centerY + circumradius * math.sin(rad))
        points.append((x, y))
    return points

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        choice = int(choice)
        return choice
    else:
        return -1

def askValue1(PPrompt: str) -> str:
    return input(f"- {PPrompt}: ")

def askValue2(PPrompt: str) -> str:
    return input(f"{PPrompt}: ")

if __name__ == "__main__":
    main()
# Note: drawLib.py file must be in the same directory as this file.