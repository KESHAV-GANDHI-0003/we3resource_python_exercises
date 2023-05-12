''' Write a Python program that calculates the area of a circle based on the radius entered by the user.'''
from math import  pi
print("Circle Area Calculator")
radius = eval(input("Enter the radius of the Circle :- "))
area_of_circle = pi*(radius**2)
print(f"Area of Cirlce with radius {radius} is :- {area_of_circle}")