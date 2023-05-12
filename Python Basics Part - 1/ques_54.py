'''Write a Python program to get the current username.'''
import getpass
print(getpass.getuser())
pswd = input("Enter password : ")
if pswd == getpass.getpass(pswd):
    print("hi")