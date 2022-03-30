# Based on the following StackOverflow article
# https://stackoverflow.com/questions/41274903/different-color-for-each-segment-of-a-pie-chart-using-turtle-in-python

from turtle import Turtle, Screen
from itertools import cycle

languages = [("Python", 50), ("C++", 10), ("Ruby", 20), (".NET", 20)]

COLORS = cycle(['green', 'yellow', 'red', 'cyan', 'white'])

RADIUS = 175
LABEL_RADIUS = RADIUS * 1.33
FONTSIZE = 18
FONT = ("Ariel", FONTSIZE, "bold")

# The pie slices

total = 100

my_turtle = Turtle()
my_turtle.penup()
my_turtle.sety(-RADIUS)
my_turtle.pendown()

for _, fraction in languages:
    my_turtle.fillcolor(next(COLORS))
    my_turtle.begin_fill()
    my_turtle.circle(RADIUS, fraction * 360 / total)
    position = my_turtle.position()
    my_turtle.goto(0, 0)
    my_turtle.end_fill()
    my_turtle.setposition(position)

# The labels

my_turtle.penup()
my_turtle.sety(-LABEL_RADIUS)

for label, fraction in languages:
    my_turtle.circle(LABEL_RADIUS, fraction * 360 / total / 2)
    my_turtle.write(label, align="center", font=FONT)
    my_turtle.circle(LABEL_RADIUS, fraction * 360 / total / 2)

my_turtle.hideturtle()

screen = Screen()
screen.exitonclick()