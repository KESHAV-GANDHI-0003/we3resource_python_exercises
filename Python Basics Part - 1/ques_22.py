'''Write a Python program to count the number 4 in a given list. '''
# Method - 1
list_1 = eval(input("Enter the list in []:- "))
count_4 = list_1.count(4)
print(f"Number 4 is repeated {count_4} times")
# Method - 2
count = 0
for i in list_1:
    if i == 4 :
        count+=1
print(f"Number 4 is repeated {count_4} times")