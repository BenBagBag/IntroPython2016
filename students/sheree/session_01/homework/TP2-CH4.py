import turtle

bob = turtle.Turtle()

window = turtle.Screen()

window.bgcolor("#421c52")

def draw_square(bob):
    for i in range(0, 4):
        bob.forward(200)
        bob.right(90)
        
draw_square(bob)

