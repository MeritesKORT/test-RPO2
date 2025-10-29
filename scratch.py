import turtle

t = turtle.Turtle()
t.color("#fbff00")

t.fillcolor("#0008ff")
t.begin_fill()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()



t = turtle.Turtle()

t.fillcolor("#fbff00")
t.begin_fill()

r = -50
t.circle(r)

t.end_fill()

turtle.done()
