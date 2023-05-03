'''
Implements a series of functions to draw common shapes with the turtle.
'''

def rectangle(turtle, length, width):
    '''
    Draws a rectangle with a given length and width.
    '''
    for i in range(0, 2):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(width)
        turtle.left(90)

def square(turtle, side_length):
    '''
    Draws a square with a given length and width.
    '''
    rectangle(turtle, side_length, side_length)