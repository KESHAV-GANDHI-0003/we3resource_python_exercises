'''Write a Python program to check whether a file exists'''
import os.path
file_name = input("Enter the File Name with extension :- ")
print(os.path.isfile(file_name))
