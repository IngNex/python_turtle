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

def dibujar_alas():
    turtle.penup()
    turtle.goto(-70, 40)
    turtle.pendown()
    turtle.left(70)
    turtle.circle(80, 150)

    turtle.penup()
    turtle.goto(70, 40)
    turtle.pendown()
    turtle.left(110)
    turtle.circle(80, -150)

def escribir_letras():
    turtle.penup()
    turtle.goto(0, 100)
    turtle.pendown()
    turtle.color("white")
    turtle.write("K", align="center", font=("Arial", 36, "bold"))
    
    turtle.penup()
    turtle.goto(0, 50)
    turtle.pendown()
    turtle.write("M", align="center", font=("Arial", 36, "bold"))

def dibujar_corazon_con_alas_y_letras():
    turtle.speed(2)
    turtle.hideturtle()
    
    dibujar_corazon()
    
    escribir_letras()

    turtle.done()

if __name__ == "__main__":
    dibujar_corazon_con_alas_y_letras()