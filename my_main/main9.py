import turtle

a = 1
b = 1

turtle.bgcolor("black")
turtle.speed(0)
turtle.pencolor("green")
while True:
    turtle.forward(a)
    turtle.left(b)
    a += 3
    b += 2
    if b == 180:
        break
turtle.done()
