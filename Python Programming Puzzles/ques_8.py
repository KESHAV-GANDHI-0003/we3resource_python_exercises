# Write a Python program to split a string of words separated by commas and spaces into two strs, words and separators.
# Input: W3resource Python, Exercises.
# Output:
# [['W3resource', 'Python', 'Exercises.'], [' ', ', ']]
# Input: The dance, held in the school gym, ended at midnight.
# Output:
# [['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]
# Input: The colors in my studyroom are blue, green, and yellow.
# Output:
# [['The', 'colors', 'in', 'my', 'studyroom', 'are', 'blue', 'green', 'and', 'yellow.'], [' ', ' ', ' ', ' ', ' ', ' ', ', ', ', ', ' ']]
def sept (str_1):
    import re
    words = []
    septt = []
    str_1 = re.split(r"([ ,?!:]+)",str_1)
    for i in str_1:
        if i.isalpha() == True:
            words.append(i)
        else:
            septt.append(i)
    print(words)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(septt)
str_1 = str(input("Enter the String :- "))
sept(str_1)