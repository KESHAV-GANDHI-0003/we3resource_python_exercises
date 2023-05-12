'''Write a Python program to calculate the difference between a given number and 17.
 If the number is greater than 17, return twice the absolute difference'''
num_1 = 17
num_2 = int(input("Enter the number :- "))
if num_2 < 17 :
    difference = num_1-num_2
    print(f"The Difference between {num_1} and {num_2} is {difference}")
elif num_2 > 17:

    difference = num_2-num_1
    difference *=2
    difference = abs(difference)
    print(f"The twice absolute difference between {num_1} and {num_2} is {difference}")