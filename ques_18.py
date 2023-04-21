'''Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum.'''
num_1 = int(input("Enter the number 1 :- "))
num_2 = int(input("Enter the number 2 :- "))
num_3 = int(input("Enter the number 3 :- "))
if num_1 == num_2 and num_2 == num_3 :
    print(f"The Sum of three numbers is {num_3+num_2+num_1}\n"*3)
else:
    print(f"The Sum of three numbers is {num_3 + num_2 + num_1}")