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

def main():
    turtle.speed(2)
    turtle.color("red")
    turtle.begin_fill()
    
    dibujar_flor(6)  # Puedes ajustar el número de pétalos según tu preferencia
    
    turtle.end_fill()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()