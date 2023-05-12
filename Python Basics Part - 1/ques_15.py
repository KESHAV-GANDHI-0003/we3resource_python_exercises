'''Write a Python program to get the volume of a sphere with radius six.'''
from math import pi
radius = eval(input("Enter the radius of sphere in cm :- "))
volume_of_sphere = (4/3)*pi*(radius**3)
print(f"The volume of sphere having radius {radius} cm is {volume_of_sphere} centimeter cube")
