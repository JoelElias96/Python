from pickle import GLOBAL
from random import randint
from turtle import Turtle,Screen
import random
ycor=-200

def init(color):
    tur=Turtle()
    tur.shape('turtle')
    tur.color(color)
    tur.penup()
    global ycor
    tur.goto(-200,ycor)
    ycor+=80
    return tur
print ("hello")

def run(tur):
    tur.forward((random.randint(1,10)))
    if tur.xcor()>=400:
        return False
    return True


screen=Screen()
screen.setup(height=400,width=500)
bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race?").lower()


red=init('red')
blue=init('blue')
green=init('green')
yellow=init('yellow')
black=init('black')
black.forward(100)


while run(red) and run(blue) and run(green) and run(yellow) and run(black):
    continue
if not run(red) and bet=="red":
    screen.title("You've won the race")
elif not run(blue) and bet=="blue":
    screen.title("You've won the race")
elif not run(green) and bet=="green":
    screen.title("You've won the race")
elif not run(yellow) and bet=="yellow":
    screen.title("You've won the race")
elif not run(black) and bet=="black":
    screen.title("You've won the race")
else:
    screen.title("You've lost the race")

screen.exitonclick()
