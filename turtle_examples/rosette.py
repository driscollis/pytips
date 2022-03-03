from turtle import Screen, Turtle, mainloop
from time import perf_counter as clock, sleep

def mn_eck(original_turtle, ne,sz):
    turtlelist = [original_turtle]
    # create ne-1 additional turtles
    for i in range(1,ne):
        cloned_turtle = original_turtle.clone()
        cloned_turtle.rt(360.0/ne)
        turtlelist.append(cloned_turtle)
        original_turtle = cloned_turtle
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let those cloned turtles make a step
        # in parallel:
        for turtl in turtlelist:
            turtl.rt(360./ne)
            turtl.pencolor(1-c,0,c)
            turtl.fd(sz)

def main():
    screen = Screen()
    screen.bgcolor("black")
    box_turtle = Turtle()
    box_turtle.speed(0)
    box_turtle.hideturtle()
    box_turtle.pencolor("red")
    box_turtle.pensize(3)

    screen.tracer(36,0)

    begin_time = clock()
    mn_eck(box_turtle, 36, 19)
    end_time = clock()
    z1 = end_time-begin_time

    sleep(1)

    begin_time = clock()
    while any(t.undobufferentries() for t in screen.turtles()):
        for t in screen.turtles():
            t.undo()
    end_time = clock()
    return "runtime: %.3f sec" % (z1+end_time-begin_time)


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

