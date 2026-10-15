import turtle
import tkinter as tk

# -------------------------
# Screen
# -------------------------
screen = turtle.Screen()
screen.setup(width=1000, height=600)
screen.title("Afnan Salehreh")
screen.bgcolor("white")

# -------------------------
# Add turtle picture
# -------------------------
canvas = screen.getcanvas()

image = tk.PhotoImage(file="turtle.png")
image = image.subsample(3, 3)

canvas.create_image(80, 120, image=image, anchor="nw")
screen.image = image


# -------------------------
# Drawing turtle
# -------------------------
t = turtle.Turtle()
t.speed(4)
t.width(4)
t.color("mediumseagreen")


# -------------------------
# Draw A
# -------------------------
def draw_A(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

    # left side
    t.setheading(70)
    t.forward(70)

    # right side
    t.right(140)
    t.forward(70)

    # line across A
    t.penup()
    t.goto(x + 12, y + 32)
    t.pendown()

    t.setheading(0)
    t.forward(35)


# -------------------------
# Draw F
# -------------------------
def draw_F(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.setheading(90)
    t.forward(70)

    t.right(90)
    t.forward(40)

    t.penup()
    t.goto(x, y + 35)
    t.pendown()

    t.setheading(0)
    t.forward(30)


# -------------------------
# Draw N
# -------------------------
def draw_N(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.setheading(90)
    t.forward(70)

    t.right(150)
    t.forward(80)

    t.left(150)
    t.forward(70)


# -------------------------
# Draw S
# -------------------------
def draw_S(x, y):

    t.penup()
    t.goto(x + 40, y + 70)
    t.pendown()

    t.setheading(180)
    t.forward(40)

    t.right(90)
    t.forward(35)

    t.right(90)
    t.forward(40)

    t.left(90)
    t.forward(35)

    t.left(90)
    t.forward(40)


# -------------------------
# Draw L
# -------------------------
def draw_L(x, y):

    t.penup()
    t.goto(x, y + 70)
    t.pendown()

    t.setheading(270)
    t.forward(70)

    t.left(90)
    t.forward(40)


# -------------------------
# Draw E
# -------------------------
def draw_E(x, y):

    t.penup()
    t.goto(x + 40, y + 70)
    t.pendown()

    t.setheading(180)
    t.forward(40)

    t.right(90)
    t.forward(70)

    t.left(90)
    t.forward(40)

    t.penup()
    t.goto(x, y + 35)
    t.pendown()

    t.setheading(0)
    t.forward(30)


# -------------------------
# Draw H
# -------------------------
def draw_H(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.setheading(90)
    t.forward(70)

    t.penup()
    t.goto(x + 40, y)
    t.pendown()

    t.setheading(90)
    t.forward(70)

    t.penup()
    t.goto(x, y + 35)
    t.pendown()

    t.setheading(0)
    t.forward(40)


# -------------------------
# Draw R
# -------------------------
def draw_R(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

    t.setheading(90)
    t.forward(70)

    t.right(90)
    t.forward(35)

    t.right(90)
    t.forward(35)

    t.right(90)
    t.forward(35)

    t.penup()
    t.goto(x + 15, y + 35)
    t.pendown()

    t.setheading(315)
    t.forward(40)


# -------------------------
# Draw Afnan
# -------------------------
draw_A(20, 50)
draw_F(80, 50)
draw_N(140, 50)
draw_A(210, 50)
draw_N(270, 50)


# -------------------------
# Draw Salehreh
# -------------------------
draw_S(20, -100)
draw_A(80, -100)
draw_L(140, -100)
draw_E(200, -100)
draw_H(260, -100)
draw_R(320, -100)
draw_E(380, -100)
draw_H(440, -100)


# -------------------------
# Draw star
# -------------------------
t.penup()
t.goto(520, -50)
t.pendown()

t.color("orange")
t.fillcolor("gold")

t.begin_fill()

for i in range(5):
    t.forward(55)
    t.right(144)

t.end_fill()


# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()