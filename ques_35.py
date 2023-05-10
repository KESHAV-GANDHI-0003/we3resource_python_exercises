'''. Write a Python program that returns true if the two given integer values are equal
or their sum or difference is 5.'''
int_1 = int(input("Enter the first integer :- "))
int_2 = int(input("Enter the second integer :- "))
def tf (num_1,num_2):
    if num_1 == num_2:
        return True
    elif num_2-num_1 == 5 or num_1-num_2 == 5 :
        return True
    else:
        return False
print(tf(int_1,int_2))