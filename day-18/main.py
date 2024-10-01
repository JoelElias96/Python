import turtle
from turtle import Turtle, Screen
import random as rd

tim = Turtle()
tim.shape('turtle')
tim.color('red')
tim.speed('fastest')
tom = Turtle()
tom.shape('turtle')
tom.color('blue')
tom.speed('fastest')
yom = Turtle()
yom.shape('turtle')
yom.color('green')
yom.speed('fastest')
scr = Screen()
ron = Turtle()
ron.shape('turtle')
ron.color('grey')
ron.speed('fastest')
cha = Turtle()
cha.shape('turtle')
cha.color('purple')
cha.speed('fastest')


def draw_square(tur):
    for i in range(4):
        tur.forward(100)
        tur.right(90)


def alternate_draw(tur):
    for i in range(25):
        tur.pendown()
        tur.forward(2)
        tur.penup()
        tur.forward(2)


def all_shapes(tur):
    tur.penup()
    tur.right(90)
    tur.forward(200)
    tur.left(90)
    tur.pendown()
    for i in range(3, 16):
        rad = 360 / i
        scr.colormode(255)
        tur.pencolor((rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
        for _ in range(i):
            tur.forward(100)
            tur.left(rad)


def random_walk(tur):
    n = 0
    tur.pensize(10)
    scr.colormode(255)
    while n != 100:
        n = rd.randint(1, 100)
        tur.pencolor((rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
        if n < 10:
            tur.right(90)
        elif n < 20:
            tur.left(90)
        elif n < 30:
            tur.forward(5)
        elif n < 40:
            tur.forward(25)
        elif n < 50:
            tur.forward(10)
        elif n < 60:
            tur.backward(25)
        elif n < 70:
            tur.backward(5)
        elif n < 80:
            tur.backward(10)
        elif n < 90:
            tur.forward(30)
        elif n < 100:
            tur.forward(20)


def better_rd_walk(tur):
    tur.pensize(10)
    scr.colormode(255)
    for i in range(200):
        tur.pencolor((rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
        tur.forward(20)
        tur.setheading(rd.choice([0, 90, 180, 270]))


def spirograph(tur, size):
    scr.colormode(255)
    for i in range(360 // size):
        tur.pencolor((rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
        tur.circle(100)
        tur.left(size)
    scr.exitonclick()


draw_square(tim)
alternate_draw(tom)
all_shapes(yom)
random_walk(ron)
better_rd_walk(ron)
spirograph(cha, 5)

import prettytable
