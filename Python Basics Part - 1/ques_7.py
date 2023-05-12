'''Write a Python program that accepts a filename from the user and prints the extension of the file. '''
file_name = input("Enter the file name with extension :- ")
file_name=file_name.split(".")
file_extension = file_name[-1]
print(f"Extension of file is {file_extension}")