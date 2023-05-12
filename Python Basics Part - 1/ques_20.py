'''Write a Python program that returns a string that is n (non-negative integer) copies of a given string.'''
def string_replicator(string, no_of_copies):
    final_string = ""
    for i in range(no_of_copies):
        final_string += string
    return (f"Final Resulted String :- {final_string}")
string = input("Enter the string :- ")
no_of_copies = int(input("Enter the no of copies :- "))
print(string_replicator(string,no_of_copies))