"""  Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.
Input:
PytHon ExerciSEs
Output:
373
Input:
JavaScript
Output:
157"""
def ASCII_sum(string):
    sum=0
    for i in string:
        if i.isupper() == True:
            sum+=ord(i)
    return sum
string = str(input("Enter the String :- "))
print(ASCII_sum(string))