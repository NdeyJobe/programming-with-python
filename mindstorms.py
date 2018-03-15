import turtle

def draw_shape ():
    window = turtle.Screen ()
    window.bgcolor ("red")
    
    brad = turtle.Turtle ()
    brad.shape("turtle")
    brad.color("green")
    brad.speed("3")
    side = 4
    count = 0
    while count < side:
        brad.forward(100)
        brad.right(90)
        count += 1
  

    angie = turtle.Turtle()
    angie.circle(100)
    angie.shape("arrow")
    angie.color("blue")


    sami = turtle.Turtle ()
    sami.forward(150)
    sami.right (45)
    sami.backward(200)
    sami.right (45)
    sami.forward(150)
    sami.right (45)
    sami.shape ("circle")
    sami.color ("pink")

    window.exitonclick()


draw_shape ()
