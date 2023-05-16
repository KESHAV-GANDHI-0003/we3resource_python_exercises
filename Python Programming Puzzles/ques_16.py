"""  Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[("oe",('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[] """
def tup_extract(list_1):
    tup_ = list_1[0]
    substring = tup_[0]
    strings = tup_[1]
    return tup_, substring, strings
def substring_check(substring,strings):
    return [s for s in strings if substring in s]
list_1 = eval(input("Enter the list using [] :- "))
tup_,substring, strings = tup_extract(list_1)
print(substring_check(substring,strings))