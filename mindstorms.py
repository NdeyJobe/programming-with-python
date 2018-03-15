import turtle

def draw_art(some_turtle):
    side = 4
    count = 0
    while count < side:
        some_turtle.forward(100)
        some_turtle.right(90)
        count += 1  

def draw_figure (): 
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
    
draw_figure ()

def draw_shape ():
    window = turtle.Screen ()
    window.bgcolor ("red")
    
    brad = turtle.Turtle ()
    brad.shape ("turtle")
    brad.color ("green")
    brad.speed ("3")
    
    for i in range (1, 37):
        draw_art (brad)
        brad.right (10)
    window.exitonclick()
    
draw_shape()

    
  





