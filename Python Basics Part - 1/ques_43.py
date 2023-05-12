'''Write a Python program to get OS name, platform and release information.'''
import os
import platform
print(f"OS Name :- {os.name}")
print(f"OS Platform :- {platform.system()}")
print(f"OS Release :- {platform.release()}")
