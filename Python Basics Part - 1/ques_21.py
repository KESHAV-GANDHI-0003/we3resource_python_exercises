'''Write a Python program that determines whether a given number (accepted from the user) is even or odd,
and prints an appropriate message to the user.'''
num_1 = int(input("Enter the number :- "))
if num_1 % 2 == 0:
    print(f"The number {num_1} is even")
else:
    print(f"The number {num_1} is odd")