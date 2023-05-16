#  Write a Python program to find strings in a given list starting with a given prefix.
# Input:
# [( ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
# Output:
# ['dog', 'donut']
list_1 = [("do",('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
def tup_extract(list_1):
    tup_ = list_1[0]
    prefix = tup_[0]
    strings = tup_[1]
    return tup_, prefix, strings
def prefix_check(prefix,strings):
    result = []
    for i in strings:
        if prefix in i[:3]:
            result.append(i)
    return result
tup_,prefix, strings = tup_extract(list_1)
print(prefix_check(prefix,strings))