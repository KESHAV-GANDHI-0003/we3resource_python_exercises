'''Write a Python program that will accept the base and height of a triangle and compute its area'''
def triangle_area_calculator(base,height):
    area_of_traingle = 1/2*base*height
    return (f"The area of triangle with base {base}cm and height {height}cm is {area_of_traingle} cm square")
print("~~~~~~Traingle Area Calculator~~~~~~")
base = eval(input("Enter the base of triangle in cm :- "))
height = eval(input("Enter the height of triangle in cm :- "))
print(triangle_area_calculator(base,height))