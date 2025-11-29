from svgwrite import Drawing, cm
from svgwrite.shapes import Rect, Circle, Polygon
from pathlib import Path
#Tämän avulla ohjelma voi löytää avattavan tiedoston
ROOT_DIR = Path(__file__).parent

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    """
    Add a square to the drawing.
    Parameters:
        PDwg: Drawing object to add the square to.
        left: X-coordinate of the left edge.
        top: Y-coordinate of the top edge.
        sideLength: Length of the square's sides.
        color: Fill color of the square.
        strokeColor: Stroke color of the square.
    """
    PDwg.add(Rect(insert=(left, top), size=(sideLength, sideLength), fill=color, stroke=strokeColor))


def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    """
    Add a circle to the drawing.
    Parameters:
        PDwg: Drawing object to add the circle to.
        centerX: X-coordinate of the circle center.
        centerY: Y-coordinate of the circle center.
        radius: Radius of the circle.
        color: Fill color of the circle.
        stroke: Stroke color of the circle.
    """
    PDwg.add(Circle(center=(centerX, centerY), r=radius, fill=color, stroke=stroke))

def drawPolygon(PDwg: Drawing, points, color, stroke) -> None:
    """
    Add a polygon to the drawing.
    Parameters:
        PDwg: Drawing object to add the polygon to.
        points: List of (x, y) tuples representing the polygon vertices.
        color: Fill color of the polygon.
        stroke: Stroke color of the polygon.
    """
    PDwg.add(Polygon(points=points, fill=color, stroke=stroke))

def saveSvg(PDwg: Drawing, file) -> None:
    """
    Save the drawing to an SVG file.
    Parameters:
        PDwg: Drawing object to save.
        file: Filename to save the SVG as.
    """
    file_location = ROOT_DIR / file #Tarkentaa tiedoston sijainnin, etsii avattavan tiedoston kansiosta Tekstitiedostot
    PDwg.saveas(file_location, pretty=True)