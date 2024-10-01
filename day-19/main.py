from turtle import Turtle, Screen

tim=Turtle()
scr=Screen()
tim.speed("fastest")

def clockWise():
    tim.right(10)

def moveUp():
    tim.forward(10)


def backClockWise():
    tim.left(10)


def moveDown():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def quit():
    exit()

scr.listen()
scr.onkey(key="Up" ,fun=moveUp)
scr.onkey(key="Down" ,fun=moveDown)
scr.onkey(key="Right" ,fun=clockWise)
scr.onkey(key="Left" ,fun=backClockWise)
scr.onkey(key="q" ,fun=quit)
scr.onkey(key="c" ,fun=clear)
scr.exitonclick()
