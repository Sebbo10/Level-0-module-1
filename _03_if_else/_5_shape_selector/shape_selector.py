import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    tooty=turtle.Turtle()
    tooty.pencolor('red')
    tooty.color('black')
    tooty.speed(0)
    # Ask the user what shape they want to draw and store it in a variable
    shape=simpledialog.askstring(title= "Shape", prompt="Give me a shape (square triangle or circle)")
    # Draw the shape requested by the user using if-elif-else statements
    if shape=="square":
        tooty.circle(radius=60, steps=4)
    if shape=="circle":
        tooty.circle(radius= 80)
    if shape=="triangle":
        tooty.circle(radius=80,steps=3)
    # Call the turtle .done() method
    window.mainloop()
