""" Write a Python program to check, for each string in a given list, 
whether the last character is an isolated letter or not. Return True otherwise False.
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True] """
def isolated_letter_chk(list_):
    output = []
    for i in list_:
        if i[-2] == " ":
            output.append(True)
        else:
            output.append(False)
    return output
list_ = eval(input("Enter the list :- "))
print(isolated_letter_chk(list_))