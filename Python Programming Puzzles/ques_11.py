# Write a Python program to find the indexes of numbers in a given list below a given threshold.
# Original list:
# [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]
# Threshold: 100
# Check the indexes of numbers of the said list below the given threshold:
# [0, 1, 2, 3, 7, 8, 9, 10]
# Original list:
# [0, 12, 4, 3, 49, 9, 1, 5, 3]
# Threshold: 10
# Check the indexes of numbers of the said list below the given threshold:
# [0, 2, 3, 5, 6, 7, 8]
list_1 = eval(input("Enter the list using [] :- "))
threshold = eval(input("Enter the threshold :- "))
def threshold_index_finder (list_1, threshold):
    index = []
    for i in list_1:
        if i < threshold:
            i = list_1.index(i)
            index.append(i)
    return index
print(threshold_index_finder(list_1, threshold))