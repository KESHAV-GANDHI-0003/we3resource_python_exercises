# Write a Python program to find a list of integers containing exactly four distinct values, 
# such that no integer repeats twice consecutively among the first twenty entries.
# Input:
# [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Output:
# True
# Input:
# [1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3]
# Output:
# False
# Input:
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
# Output:
# False
list_1 = eval(input("Enter the list using [] :- "))
dec = True
list_2 = list_1[0:4]
for i in list_2:
    count = list_2.count(i)
    if count >= 2:
        print(count)
        dec = False
        break
if dec == True:
    print(True)