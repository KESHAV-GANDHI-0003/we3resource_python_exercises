# Given a string consisting of whitespace and groups of matched parentheses, 
# write a Python program to split it into groups of perfectly matched parentheses without any whitespace.
# Input:
# ( ()) ((()()())) (()) ()
# Output:
# ['(())', '((()()()))', '(())', '()']
# Input:
# () (( ( )() ( )) ) ( ())
# Output:
# ['()', '((()()()))', '(())']
list_1 = []
def Push(item):
    list_1.append(item)
def sept (str_1):
    item = ""
    left_brack_count = 0
    right_brack_count = 0
    for i in str_1:
        if i == "(":
            item +=i
            left_brack_count+=1
        elif i == ")":
            item +=i
            right_brack_count+=1
        if left_brack_count == right_brack_count and left_brack_count != 0:
            left_brack_count = 0
            right_brack_count = 0
            Push(item)
            item = ""
    return list_1
str_1 = "() (( ( )() ( )) ) ( ())"
print(sept(str_1))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
str_2 = "( ()) ((()()())) (()) ()"
list_1 = []
print(sept(str_2))