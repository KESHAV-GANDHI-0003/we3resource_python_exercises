# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
# Input:
# 922
# Output:
# True
# Input:
# 914
# Output:
# False
# Input:
# 854
# Output:
# True
# Input:
# 854
# Output:
# True
int_1 = int(input("Enter the integer :- "))
#  Here 4 mod 34 means X = int_1 and Y = 34 , X mod 34 = 4
if int_1 > 4**4 and int_1 % 34 == 4:
    print(True)
else:
    print(False)