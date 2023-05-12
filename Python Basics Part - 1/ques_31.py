'''Write a Python program that computes the greatest common divisor (GCD) of two positive integers'''
from math import gcd
# Method - 1
# int_1 = int(input("Enter first integer :- "))
# int_2 = int(input("Enter second integer :- "))
# gcd_ = gcd(int_1,int_2)
# print(f"Greatest common divisor (GCD) of two {int_1} , {int_2} is {gcd_}")
# Method - 2
int_1 = int(input("Enter the first integer :- "))
int_2 = int(input("Enter the second integer :- "))
common_factors = []
def factors_finders(integer):
    while True:
        for i in range(2,15):
            if integer % i == 0:
                integer= integer/i
                common_factors.append(i)
        if integer == 1:
            break
factors_finders(int_1)
factors_finders(int_2)
def gcd_finder (common_factors):
    global gcd_
    gcd_ = 1
    common_factors = set(common_factors)
    for i in common_factors:
        gcd_ *= i
    return gcd_
print(common_factors)
print(gcd_finder(common_factors))
