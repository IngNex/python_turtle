import turtle

def dibujar_petalo():
    turtle.circle(100, 60)
    turtle.left(120)
    turtle.circle(100, 60)
    turtle.left(120)

def dibujar_flor(num_petelos):
    for _ in range(num_petelos):
        dibujar_petalo()
        turtle.right(360 / num_petelos)

def dibujar_tallo():
    turtle.color("green")
    turtle.pensize(10)
    turtle.right(90)
    turtle.forward(300)

def dibujar_flor_completa(num_petelos):
    turtle.speed(2)
    
    turtle.begin_fill()
    turtle.color("red")
    dibujar_flor(num_petelos)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    
    dibujar_tallo()

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    dibujar_flor_completa(6)