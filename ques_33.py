'''' Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero. '''
int_1 = int(input("Enter the first integer :- "))
int_2 = int(input("Enter the second integer :- "))
int_3 = int(input("Enter the third integer :- "))
sum = 0
if int_1 == int_2 or int_3 == int_2 or int_3 == int_1:
    sum = 0
    print(f"The Sum of {int_1}, {int_2}, {int_3} is {sum}")
else:
    sum = int_1+int_2+int_3
    print(f"The Sum of {int_1}, {int_2}, {int_3} is {sum}")