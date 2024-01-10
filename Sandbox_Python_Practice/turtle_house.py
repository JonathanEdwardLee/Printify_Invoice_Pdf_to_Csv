# create a function to draw a house with turtle
# Jonathan Lee

import turtle

turtle.shape("turtle")
turtle.speed(5)
turtle.color("orange")
turtle.bgcolor("black")

def square(len):
    for i in range(4):
        turtle.forward(len)
        turtle.right(90)
    
def triangle(len):
    for i in range(3):
        turtle.forward(len)
        turtle.left(120)

def place(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def house(len):
    square(len)
    triangle(len)

place(-50,0)
house(50)
place(50,50)
house(100)



# def polygon(num_sides, size):
#     for _ in range(num_sides):
#         turtle.forward(size)
#         turtle.left(360 / num_sides)

# def draw_house(x, y):
#     # Move the turtle to the starting position for the square
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()

#     # Draw square (base of the house)
#     turtle.color('orange')
#     for _ in range(4):
#         turtle.forward(100)
#         turtle.left(90)

#     # Move the turtle to the starting position for the roof
#     turtle.penup()
#     turtle.goto(x, y + 100)
#     turtle.pendown()
#     turtle.setheading(60)  # Orient the turtle for the roof

#     # Draw triangle (roof of the house)
#     for _ in range(3):
#         turtle.forward(100)
#         turtle.right(120)

#     # Reset the turtle orientation
#     turtle.setheading(0)

# def main():
#     draw_house(-150, 0)  # Draw the first house
#     draw_house(50, 0)    # Draw the second house

# main()

turtle.Screen().exitonclick()


