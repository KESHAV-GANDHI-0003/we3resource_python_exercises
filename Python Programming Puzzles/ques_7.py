# Write a Python program to check a given list of integers where the sum of the first i integers is i.
# Input:
# [0, 1, 2, 3, 4, 5]
# Output:
# False
# Input:
# [1, 1, 1, 1, 1, 1]
# Output:
# True
# Input:
# [2, 2, 2, 2, 2]
# Output:
# False
def isumchk(list_ , i):
    if sum(list_[:i]) == i:
        return True
    else:
        return False
print(isumchk([0, 1, 2, 3, 4, 5], 5))