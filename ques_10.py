'''Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.'''
num = int(input("Enter the number :- "))
num_1 = int("%s" % num)
num_2 = int("%s%s" % (num,num))
num_3 = int("%s%s%s" % (num,num,num))
print(f"Result :- {num_1+num_2+num_3}")