'''Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2)'''
start = eval(input("Enter the starting point using () :- "))
end = eval(input("Enter the final point using () :- "))
x1,y1 = start[0], start[1]
x2,y2 = end[0], end[1]
distance = (((x2-x1)**2)+((y2-y1)**2)**1/2)
print(f"Distance between {start} and {end} is {distance}")

