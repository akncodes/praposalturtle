# pip install turtle
# USING TURTLE LIBRARY


import turtle
#The turtle module provides turtle graphics primitives, in both object-oriented and procedure-oriented ways. 
s = turtle.Screen().bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(15)

def curve():
    for i in range(0, 500):
        t.right(1)
        t.forward(1)

def main():
    t.color('red', 'blue')
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()


if __name__ == "__main__":
    main()
    t.penup()
    t.goto(-280, -20)
    t.pencolor('blue')
    t.write("I  YOU", align='left', font=("courier", 150, 'bold italic'))
