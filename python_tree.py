import turtle

def dibujar_corazon():
    turtle.color("red")
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    turtle.end_fill()

def escribir_letras():
    turtle.penup()
    turtle.goto(0, 70)
    turtle.pendown()
    turtle.color("white")
    turtle.write("K", align="center", font=("Arial", 24, "normal"))
    turtle.penup()
    turtle.goto(0, 20)
    turtle.pendown()
    turtle.write("M", align="center", font=("Arial", 24, "normal"))

def dibujar_corazon_con_letras():
    turtle.speed(2)
    turtle.hideturtle()
    
    dibujar_corazon()
    escribir_letras()

    turtle.done()

if __name__ == "__main__":
    dibujar_corazon_con_letras()