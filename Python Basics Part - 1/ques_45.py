# ''' Write a Python program that calls an external command.'''
# from subprocess import call
# call(["ls", "-l"])
# import os
# print(os.system('ls -l'))

import psutil
print(psutil.cpu_count())