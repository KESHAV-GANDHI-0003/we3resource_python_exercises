'''Write a Python program to print to STDERR.'''
from __future__ import print_function
import sys
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
eprint("abc" , "hkg","dkgh" , sep = "--")
print("abc" , "hkg","gh" , sep = "--")