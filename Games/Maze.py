import turtle as trtl
import MazeLib as mm


wn = trtl.Screen()
GridTrtl = trtl.Turtle()
Runner = trtl.Turtle()
PathCreator = trtl.Turtle()
Solver = trtl.Turtle()
GridTrtl.speed(0)
GridTrtl.color("black")
Runner.color("black")
Solver.color("blue")
Runner.speed(0)
PathCreator.color("white")
PathCreator.speed(0)
PathCreator.left(90)
PathCreator.hideturtle()
Solver.hideturtle()
yertle = trtl.Turtle('turtle')
yertle.speed('fastest')
yertle.color('green')
yertle.turtlesize(.8)

yertle.penup()
yertle.goto(-((mm._width * 10) - 5), (mm._width * 10) + 5)
yertle.pendown()

def dragging(x, y):
    yertle.ondrag(None)
    yertle.setheading(yertle.towards(x, y))
    yertle.goto(x, y)
    yertle.ondrag(dragging)

yertle.ondrag(dragging)
mm.DrawGrid(GridTrtl, wn)
mm.Start(Runner, PathCreator, Solver, wn)



wn.mainloop()
