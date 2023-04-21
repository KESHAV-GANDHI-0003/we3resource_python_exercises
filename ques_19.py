'''Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".'''
string_1 = input("Enter the string :- ")
if string_1.startswith("Is"):
    print(string_1)
else:
    print("Is"+string_1)