# by Jonathan Lee

import turtle

screen = turtle.Screen()
screen.bgcolor("black")

turtle1 = turtle.Turtle()
turtle1.color("cyan")
turtle1.speed(0)
turtle1.pensize(2)

turtle2 = turtle.Turtle()
turtle2.color("magenta")
turtle2.speed(0)
turtle2.pensize(2)

def move_turtle(turtle_obj, distance):
    turtle_obj.penup()  
    turtle_obj.backward(distance)
    turtle_obj.right(distance)  
    turtle_obj.pendown()

def turtle_goto(turtle_obj,x,y):
    turtle_obj.penup()
    turtle_obj.goto(x,y)
    turtle_obj.pendown()



def bluestar(x,y):
    for i in range(5):
        turtle1.forward(x) #100
        turtle1.right(y) #144
    move_turtle(turtle1,20)

def redstar(x,y):
    for i in range(5):
        turtle2.forward(x) #100
        turtle2.right(y) #144
    move_turtle(turtle2,20)

def repeat_star(x):
    for i in range(x):
        redstar(100,144)
        bluestar(100,144)

def main():
    bluestar(100,144)
    move_turtle(turtle2,10)
    repeat_star(17)

main()
turtle_goto(turtle2,-1,7)
turtle2.circle(50)
turtle_goto(turtle1,-9,-98)
turtle1.circle(155)




turtle1.hideturtle()
turtle2.hideturtle()


screen.mainloop()
