'''Write a Python program that checks whether a specified value is contained within a group of values.
Test Data :
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''
list_1 = eval(input("Enter the list using [] :- "))
num = int(input("Enter the number :- "))
if num in list_1:
    print(f"The number {num} is present in list.")
else:
    print(f"The number {num} is not present in list.")