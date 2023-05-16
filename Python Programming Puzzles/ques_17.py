"""  Write a Python program to create a string consisting of non-negative integers up to n inclusive.
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 """
def no_string_creator (n):
    string = ""
    strings = [x for x in range(n+1)]
    for x in strings:
        string = string + str(x) + " "
    return string
n = int(input("Enter the n :- "))
print(no_string_creator(n))
    