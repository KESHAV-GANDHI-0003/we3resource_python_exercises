'''Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.'''
int_1 = int(input("Enter the first integer  :- "))
int_2 = int(input("Enter the second integer  :- "))
sum = int_2+int_1
if 15 < sum < 20:
    print(print(f"The Sum of {int_1}, {int_2} is {20}"))
else:
    print(f"The Sum of {int_1}, {int_2} is {sum}")