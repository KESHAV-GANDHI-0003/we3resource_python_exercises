""" Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence! """
def monotonic_seq_chk(list_):
    if list_ [0] < list_[1]:
        return "Increasing"
    elif list_[0] > list_[1]:
        return "Decreasing"
    elif list_[0] == list_[1]:
        return "Not a monotonic Sequence"
list_ = eval(input("Enter the list :- "))
print((monotonic_seq_chk(list_)))
