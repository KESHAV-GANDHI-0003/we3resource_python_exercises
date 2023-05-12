'''Write a Python program to test whether a passed letter is a vowel or not.'''
vowels = ["a","e","i","o","u"]
letter = input("Enter the letter you want to check :- ")
letter_1 = letter.lower()
if letter_1 in vowels:
    print(f"The letter {letter} is a vowel.")
else :
    print(f"The letter {letter} is not a vowel.")