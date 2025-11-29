# A8_T6 Scalable Vector Graphics (TEST TASK)
# Use svgwrite==1.4.3 library or build your own custom library to draw SVGs(Scalable Vector Graphics).

# Links to get started with svgwrite

# Latest svgwrite documentation: https://svgwrite.readthedocs.io/en/latest/
# Package in Pypi: https://pypi.org/project/svgwrite/
# Create menu-driven program with following options:

# Draw square (rectangle with both sides same length)
# Draw circle
# Save svg
# Exit
# Start the program creation by initialising Drawing and then define functions to fill in the details. Remember, passing object in Python works as reference to the memory.

# from svgwrite import Drawing, cm
# from svgwrite.shapes import Rect, Circle, Polygon

# def drawSquare(PDwg: Drawing) -> None:
#     # ...
#     PDwg.add(Rect(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#rect
#     return None

# def drawCircle(PDwg: Drawing) -> None:
#     # ...
#     PDwg.add(Circle(...)) # See https://svgwrite.readthedocs.io/en/latest/classes/shapes.html#circle
#     return None

# def saveSvg(PDwg: Drawing) -> None:
#     # See Drawing.save method https://svgwrite.readthedocs.io/en/latest/classes/drawing.html?highlight=save#svgwrite.drawing.Drawing.save
#     return None

# def main() -> None:
#     # 1. Initialise
#     Dwg = svgwrite.Drawing()
#     # ...
#         drawSquare(Dwg)
#         drawCircle(Dwg)
#     # 3. Cleanup
#     return None

# Make the program save the created .svg in pretty format with 2 space indentations. Before saving, ensure the write operation from user by repeating the filename to write and then ask to proceed (y/n).
from drawLib import drawCircle, drawSquare, saveSvg, Drawing

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
            case 3:
                filename = askValue2("Filename")
                print(f'Saving to file "{filename}"')
                proceed = askValue2("Proceed (y/n)?")
                if proceed.lower() == 'y':
                    saveSvg(Dwg, filename)
                    print("Vector saved successfully!")
                else:
                    print("Save cancelled.")
                
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
    print("3 - Save svg")
    print("0 - Exit")

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