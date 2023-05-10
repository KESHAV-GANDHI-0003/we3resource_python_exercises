'''Write a Python program to list all files in a directory.'''
from os import listdir
from os.path import isfile, join
flie_list = [f for f in listdir("C/GANDH") if isfile(join('C/GANDH',f))]