# Write a Python program to check whether the given strings are palindromes or not. Return True otherwise False.
# Input:
# ['palindrome', 'madamimadam', '', 'foo', 'eyes']
# Output:
# [False, True, True, False, False]
def palindrome_checker (string):
    if string == string[::-1]:
        return True
    else:
        return False
def palindrome_check_list (list_of_strings):
    for string in list_of_strings:
        if palindrome_checker(string) == True:
            palindrome_result.append("True")
        else:
            palindrome_result.append("False")   
    return palindrome_result
palindrome_result = []
print(palindrome_check_list(['palindrome','madamimadam', '', 'foo', 'eyes']))