import turtle as t 

t.speed(0)
t.bgcolor("black")
t.pencolor("cyan")
def square(x,  y):
    for i in range(100):
        t. forward(x)
        t. right(y)
for i in range(80):
    square(400, 35)
    t.right(15)
    t.circle(100)
    t.right(80)
    t.hideturtle()
t.done()