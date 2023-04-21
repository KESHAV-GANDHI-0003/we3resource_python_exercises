''' Write a Python program that concatenates all elements in a list into a string and returns it.'''
list_1 = eval(input("Enter the list using [] :- "))
string = ""
for i in list_1:
    string+=str(i)
print(f"The concatenated string of list {list_1} is {string}")