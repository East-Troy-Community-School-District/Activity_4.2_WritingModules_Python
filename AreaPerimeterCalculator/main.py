'''
Area Perimeter Calculator
Pawelski
5/2/2023
Python II

Instructions
How does this program use the area module to break up the program?
Modify the program by writing the perimeter module to calculate the
perimeter for the same shapes represented in the area module. What
did you need to do in the main module?
'''

import area

repeat = "y"
while repeat == "y":
    calculation_type = input("Do you need to calculate an area or perimeter? >> ")
    if calculation_type == "area":
        area.select_shape()
    elif calculation_type == "perimeter":
        pass
    else:
        print("Invalid operation!")
    repeat = input("Would you like to calculate another area or perimeter? (y/n) >> ")
    print()