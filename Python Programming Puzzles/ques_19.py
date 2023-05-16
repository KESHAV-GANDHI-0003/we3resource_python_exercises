""" Write a Python program to split a given string (s) into strings if there is a space in s, 
otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd
order (order of a = 0, b = 1, etc.).
Input:
a b c d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
a,b,c,d
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['a', 'b', 'c', 'd']
Input:
abcd
Split the said string into strings if there is a space in the string,
otherwise split on commas if there is a comma,
Output:
['b', 'd'] """
def space_splitter (string):
    return string.split(" ")
def comma_splitter (string):
    return string.split(",")
def odd_list (string):
    return [string[x] for x in range(len(string)) if x % 2 == 1]
def string_categorise (string):
    if "," in string:
        return comma_splitter(string)
    elif " " in string:
        return space_splitter(string)
    else:
        return odd_list(string)
string = str(input("Enter the String :- "))
print(string_categorise(string))