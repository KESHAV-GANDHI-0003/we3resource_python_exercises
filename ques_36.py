'''Write a Python program to add two objects if both objects are integers'''
def addnum(num_1,num_2):
    sum = num_1+num_2
    return sum
num_1 = eval(input("Enter the first integer :- "))
num_2 = eval(input("Enter the second integer :- "))
if type(num_1) == type(2) and type(num_2) == type(5):
    sum = addnum(num_1,num_2)
    print(f"The sum of {num_1} and {num_2} is {sum}")
else:
    print("Both are not integers")