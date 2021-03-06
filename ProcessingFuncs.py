import arcade

fillColor = arcade.color.WHITE
strokeColor = arcade.color.BLACK
strokeThickness = 1
isStroke = True
inShape = False
isFill = True
vertexList = []

def noFill():
    isFill = False

def fill(color):
    isFill = True
    fillColor = color

def noStroke():
    isStroke = False
    
def stroke(color):
    isStroke = True
    strokeColor = color

def strokeWidth(wid):
    strokeTickness = wid

def point(x, y):
    arcade.draw_circle_filled(x, y, strokeColor, strokeThickness)

def line(x1, y1, x2, y2):
    arcade.draw_line(x1, y1, x2, y2, strokeColor, strokeThickness)

def circle(x, y, radius):
    if (isFill):
        arcade.draw_circle_filled(x, y, radius, fillColor)
    if (isStroke):
        arcade.draw_circle_outline(x, y, radius, fillColor, strokeThickness)

def ellipse(x, y, rx, ry, **kwargs):
    if (isFill):
        arcade.draw_ellipse_filled(x, y, rx, ry, fillColor)
    if (isStroke):
        arcade.draw_ellipse_outline(x, y, rx, ry, fillColor, strokeThickness)

def polyline(vertices):
    if (isFill):
        arcade.draw_polygon_filled(vertices, fillColor)
    if (isStroke):
        arcade.draw_polygon_outline(vertices, strokeColor, strokeThickness)

def rect(cx, cy, w, h):
    if (isFill):
        arcade.draw_rect_filled(cx, cy, w, h, fillColor)
    if (isStroke):
        arcade.draw_polygon_outline(cx, cy, w, h, strokeColor, strokeThickness)

def beginShape():
    if inShape:
        print("Error: already in shape.")
        return
    inShape = True

def addVertex(x, y):
    vertexList.append((x, y))

def endShape():
    if not inShape:
        print("Error: Not in shape.")
        return
    polyline(vertexList)
    inShape = False
    vertexList = []
