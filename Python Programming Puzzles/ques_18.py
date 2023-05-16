""" An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. 
Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them,
but they are useful as arrays in computing.
Write a Python program to find the indices of all occurrences of target in the uneven matrix.
Input:
[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
Output:
[[0, 4], [1, 0], [1, 3], [4, 1]]
Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
Output:
[[0, 1], [0, 3], [2, 2]] """
def extract (list__):
    target = list__[1]
    tup_ = list__[0]
    return tup_,target

def fn (tpu_, target):
    result = []
    for i in range(len(tpu_)):
            if tpu_[i] == []:
                continue
            else:
                for j in range(len(tpu_[i])):
                    if tup_[i][j] == target:
                        result.append([i,j])
    return result
list__ = [([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
tup_ , target = extract(list__)
print(tup_)
print(fn(tup_, target))