import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    simpledialog.askinteger(title="Radius", prompt="What is the radius")
    # Make a new turtle
    tooty=turtle.Turtle
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    tooty.circle(radius=19)
    # Call the turtle .penup() method
    tooty.penup()
    # Move your turtle to a new x,y position using .goto()
    tooty.goto(50,30)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area=1134.11
    # Write the area of your circle using the turtle .write() method
    tooty.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    tooty.hideturtle()
    # Call turtle.done()
    tooty.done()

