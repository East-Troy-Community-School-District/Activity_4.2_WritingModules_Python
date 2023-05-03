'''
Turtle Shapes
Pawelski
5/2/2023
Python II

Instructions
What is the name of the project folder? What is the name of the file
with the actual program code? What is the name of the user-defined
module in this project? How did we get access to this module? What
is inside this module? What docstring is new? Why is it important
to write the docstrings for the module and each function? How do we
call a function in the shapes module from the main module?
Why? What happens if we move the shapes module outside the project
folder? What happens if we run the shapes module?

Finally, let's add the triangle() function to the shapes module. Test
the function by calling it in the main module. Why do we need to pass
the turtle into the function?
'''

import turtle
import shapes

t = turtle.Turtle()

# Draw a rectangle
shapes.rectangle(t, 50, 100)

# Move to new location and draw square
t.penup()
t.goto(100, 100)
t.pendown()
shapes.square(t, 50)
turtle.done()