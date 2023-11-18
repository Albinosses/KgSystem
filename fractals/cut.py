import turtle
from PIL import Image


def setup_turtle():
    # Налаштування вікна для малювання
    screen = turtle.Screen()
    screen.setup(width=700, height=700)
    screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
    screen.bgcolor("white")

    # Створення об'єкта черепашки
    fractal_turtle = turtle.Turtle()
    fractal_turtle.penup()
    fractal_turtle.goto(5, 5)
    fractal_turtle.pendown()
    fractal_turtle.speed(0)

    return fractal_turtle, screen


def build_fractal_side(turtle, order, length):
    if order == 0:
        turtle.forward(length)
    else:
        build_fractal_side(turtle, order - 1, length / 2)
        turtle.left(85)
        build_fractal_side(turtle, order - 1, length / 2)
        turtle.right(170)
        build_fractal_side(turtle, order - 1, length / 2)
        turtle.left(85)
        build_fractal_side(turtle, order - 1, length / 2)


def build_cut_fractal(order):
    fractal_turtle, screen = setup_turtle()
    length = 500
    for _ in range(4):
        build_fractal_side(fractal_turtle, order, length)
        fractal_turtle.left(90)
    save_fractal_image(screen)


def save_fractal_image(screen):
    ts = screen.getcanvas()
    ts.postscript(file="../fractal.ps", colormode='color')
    turtle.clearscreen()
    im = Image.open("../fractal.ps")
    im.save("fractal.png")
