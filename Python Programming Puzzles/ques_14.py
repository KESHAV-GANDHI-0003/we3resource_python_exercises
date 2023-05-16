""" Write a Python program to find the length of a given list of non-empty strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0] """
def string_length_finder(string_list):
    string_length_list = []
    for i in string_list:
        string_length = len(i)
        string_length_list.append(string_length)
    return string_length_list
string_list = ['cat', 'car', 'fear', 'center']
print(string_length_finder(string_list))
