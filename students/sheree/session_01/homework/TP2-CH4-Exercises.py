'''
Exercise 1  
Download the code in this chapter from http://thinkpython2.com/code/polygon.py.
Draw a stack diagram that shows the state of the program while executing circle(bob, radius). You can do the arithmetic by hand or add print statements to the code.

Figure 4.1: Turtle flowers.
Exercise 2  
Write an appropriately general set of functions that can draw flowers as in Figure 4.1.
Solution: http://thinkpython2.com/code/flower.py, also requires http://thinkpython2.com/code/polygon.py.


Figure 4.2: Turtle pies.
Exercise 3  
Write an appropriately general set of functions that can draw shapes as in Figure 4.2.
Solution: http://thinkpython2.com/code/pie.py.

Exercise 4  
The letters of the alphabet can be constructed from a moderate number of basic elements, like vertical and horizontal lines and a few curves. Design an alphabet that can be drawn with a minimal number of basic elements and then write functions that draw the letters.
You should write one function for each letter, with names draw_a, draw_b, etc., and put your functions in a file named letters.py. You can download a “turtle typewriter” from http://thinkpython2.com/code/typewriter.py to help you test your code.

You can get a solution from http://thinkpython2.com/code/letters.py; it also requires http://thinkpython2.com/code/polygon.py.

Exercise 5  
Read about spirals at http://en.wikipedia.org/wiki/Spiral; then write a program that draws an Archimedian spiral (or one of the other kinds). Solution: http://thinkpython2.com/code/spiral.py.

----

I didn't do all of that but I made a cute shape I like. 

'''

import turtle

window = turtle.Screen()
window.bgcolor("#421C52")

def draw_square(some_turtle):
    for i in range(0,4):
        some_turtle.forward(200)
        some_turtle.right(90)
        
def draw_circle_with_square():
    purple_turtle = turtle.Turtle()
    purple_turtle.shape("circle")
    purple_turtle.speed(9)
    purple_turtle.pensize(3)
    purple_turtle.hideturtle()
    for i in range(1,37):
        if i % 2 == 0:
            purple_turtle.color("white")
        else:
            purple_turtle.color("#732C7B")
        draw_square(purple_turtle)
        purple_turtle.right(10)

#def draw_circle():
#	turtle_two = turtle.Turtle()
#	turtle_two.shape("arrow")
#	turtle_two.color("white")
#	turtle_two.circle(100)
#	
#def draw_triangle():
#	turtle_three = turtle.Turtle()
#	turtle_three.shape("turtle")
#	turtle_three.color("black")
#	turtle_three.backward(100)
#	turtle_three.left(60)
#	turtle_three.forward(100)
#	turtle_three.right(120)
#	turtle_three.forward(100)

draw_circle_with_square()
#draw_square()
#draw_circle()
#draw_triangle()

window.exitonclick()