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

def dibujar_flores():
    turtle.color("green")
    for _ in range(36):
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(30)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)
        turtle.forward(100)
        turtle.right(45)
        turtle.forward(30)
        turtle.right(45)
        turtle.forward(100)
        turtle.right(135)

def escribir_letras():
    turtle.penup()
    turtle.goto(0, 70)
    turtle.pendown()
    turtle.color("white")
    turtle.write("K", align="center", font=("Arial", 36, "bold"))

    turtle.penup()
    turtle.goto(0, 20)
    turtle.pendown()
    turtle.write("M", align="center", font=("Arial", 36, "bold"))

def main():
    turtle.speed(2)
    turtle.hideturtle()

    dibujar_corazon()
    dibujar_flores()
    escribir_letras()

    turtle.done()

if __name__ == "__main__":
    main()