import collections
import math
import turtle

SIZE = 20
Point = collections.namedtuple("Point", ["x", "y"])
Hex = collections.namedtuple("Hex", ["q", "r"])

def hex_to_pixel(hex):
    x = SIZE * math.sqrt(3) * (hex.q + hex.r/2)
    y = SIZE * 3/2 * hex.r
    return Point(x, y)

sc=turtle.Screen()
tr=turtle.Turtle()

def init_turtle():
    sc.bgcolor("lightgreen")
    sc.title("Hex")
    tr.color("blue")
    tr.pensize(3)

def draw_hex(hex):
    tr.penup()
    tr.home()
    tr.setpos(hex_to_pixel(hex))
    tr.forward(SIZE)
    tr.left(90)
    tr.pendown()
    for i in range(6):
        tr.forward(SIZE)
        tr.left(60)

init_turtle()
for i in range(-3, 3):
    for j in range(-3, 3):
        draw_hex(Hex(i, j))

tr.hideturtle()
sc.mainloop()

