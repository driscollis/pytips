import turtle


class MyTurtle(turtle.Turtle):

    def __init__(self):
        """Turtle Constructor"""
        turtle.Turtle.__init__(self, shape="turtle")
        screen = turtle.Screen()
        screen.bgcolor("lightgrey")
        self.pensize(3)

    def drawCircle(self, x, y, color, radius=50):
        """
        Moves the turtle to the correct position and draws a circle
        """
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.color(color)
        self.circle(radius)

    def drawOlympicSymbol(self):
        """
        Iterates over a set of positions to draw the Olympics logo
        """
        positions = [(0, 0, "blue"), (-120, 0, "purple"), (60,60, "red"),
                     (-60, 60, "yellow"), (-180, 60, "green")]
        for x, y, color in positions:
            self.drawCircle(x, y, color)

        self.drawText()

    def drawText(self):
        """
        Draw text to the screen
        """
        self.penup()
        self.setposition(-60, 0)
        self.setheading(0)
        self.pendown()
        self.color("black")
        self.write("Mouse vs Python", font=("Arial", 16, "bold"))

if __name__ == "__main__":
    t = MyTurtle()
    t.drawOlympicSymbol()
    turtle.getscreen()._root.mainloop()