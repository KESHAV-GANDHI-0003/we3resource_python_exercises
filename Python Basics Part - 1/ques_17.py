'''Write a Python program to test whether a number is within 100 of 1000 or 2000.'''
def near_th(num):
    if abs(1000-num) <= 100:
        return (f"Number {num} is within 100 of 1000")
    elif abs(2000-num) <= 100:
        return (f"Number {num} is within 100 of 2000")
    else:
        return (f"Number is not within 100 of 1000 or 2000")
num = eval(input("Enter the number you want to check :- "))
print(near_th(num))