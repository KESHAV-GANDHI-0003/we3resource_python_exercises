# Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.
# Input:
# ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
# Output:
# True
# Input:
# ['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
# Output:
# False
# Input:
# ['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
# Output:
# True
list_1 = eval(input("Enter the list :- "))
nth = list_1[-1]
nth_1 = list_1[-2]
if nth_1 in nth:
    print(True)
else:
    print(False)