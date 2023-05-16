'''Write a Python program that accepts a list of integers and calculates the length and the fifth element. 
Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False'''
# Method  - 1
# list_1 = eval(input("Enter the lsit using  [] :- "))
# fifth_ele = list_1[4]
# count_fifth_ele = list_1.count(fifth_ele)
# list_length = len(list_1)
# if count_fifth_ele == 3 and list_length == 8:
#     print("True")
# else:
#     print("False")
# Method - 2
list_1 = eval(input("Enter the List using [] :- "))
fifth_ele = list_1[4]
list_length = 0
count_fifth_ele = 0
for i in list_1:
    list_length+=1
    if i == fifth_ele:
        count_fifth_ele +=1
if count_fifth_ele == 3 and list_length == 8:
    print("True")
else:
    print("False")
