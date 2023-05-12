'''Write a Python program that accepts a sequence of comma-separated numbers from the user and
 generates a list and a tuple of those numbers'''
number_sequence = input("Enter the number sequence seperated by comma :- ")
number_sequence = number_sequence.split(",")
number_sequence_list = number_sequence
number_sequence_tuple = tuple(number_sequence)
print(f"List :- {number_sequence_list} \nTuple :- {number_sequence_tuple}")