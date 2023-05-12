'''Write a Python program to find a list of integers with exactly two occurrences of nineteen and
at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True'''
# Method - 1
'''list_1 = eval(input("Enter the List using [] :- "))
count_19 = list_1.count(19)
count_5 = list_1.count(5)
if count_19 == 2 and count_5 == 3:
    print("True")
else:
    print("False")'''
# Method - 2
list_1 = eval(input("Enter the List using [] :- "))
for i in list_1:
    if i == 19:
        count_19 += 1
    elif i == 5:
        count_5 += 1
print(count_19)
print(count_5)
if count_19 == 2 and count_5 == 3:
    print("True")
else: 
    print("False")