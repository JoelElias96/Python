###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

from turtle import Turtle,Screen
import random
import colorgram
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
 #   red=color.rgb.r
  #  green=color.rgb.g
   # blue=color.rgb.b
    #new_color=(red, green, blue)
   # rgb_colors.append(new_color)

herst_colors=[(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim=Turtle()
scr=Screen()
scr.colormode(255)

tim.penup()
tim.goto(-250,-250)

for _ in range(10):
    tim.goto(-250,-250+(_*50))
    for i in range(10):
        tim.dot(20,random.choice(herst_colors))
        tim.forward(50)

scr.exitonclick()