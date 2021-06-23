import turtle
turtle.title('rectanguloid')
turtle.speed(8)
turtle.begin_fill()

turtle.fd(200)
turtle.right(90)
turtle.fd(100)
turtle.right(90)
turtle.fd(200)
turtle.right(90)
turtle.fd(100)

#Top
turtle.left(55)
turtle.fd(66)
turtle.right(145)
turtle.fd(200)
turtle.right(35)
turtle.fd(66)

#Right
turtle.penup()
turtle.goto(200, -100)
turtle.pendown()
turtle.left(180)
turtle.fd(66)
turtle.left(35)
turtle.fd(200)

#Back
turtle.penup()
turtle.goto(200, 0)
turtle.pendown()
turtle.right(35)
turtle.forward(66)
turtle.left(125)
turtle.forward(100)
turtle.right(90)
turtle.forward(200)

#Bottom
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.right(35)
turtle.forward(66)
turtle.right(55)
turtle.forward(100)

turtle.ht()
turtle.done()
