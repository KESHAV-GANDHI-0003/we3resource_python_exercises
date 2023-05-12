'''Write a Python program to find the least common multiple (LCM) of two positive integers. '''
no_of_int = int(input("Enter the no of integers whom LCM you have to find ::- "))
integers = []
for i in range(no_of_int):
    int_ = int(input("Enter the integer :- "))
    integers.append(int_)
for i in integers:

common_factors = []
def factors_finders(integer):
    while True:
        for i in range(2,15):
            if integer % i == 0:
                integer= integer/i
                common_factors.append(i)
        if integer == 1:
            break
# factors_finders(int_)
# def lcm_finder (common_factors):
#     global lcm_
#     lcm_ = 1
#     common_factors = set(common_factors)
#     for i in common_factors:
#         lcm_ *= i
#     return lcm_
# print(lcm_finder(common_factors))