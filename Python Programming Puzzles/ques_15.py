""" Write a Python program to find the longest string in a given list of strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter """
def long_string_finder (list_):
    string_lengths = []
    for i in list_:
        string_length = len(i)
        string_lengths.append(string_length)
    long_string = max(string_lengths)
    long_str_index = string_lengths.index(long_string)
    long_string_ = list_[long_str_index]
    return long_string_
list_ = eval(input("Enter the list using [] :- "))
print(long_string_finder(list_))