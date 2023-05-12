'''Ques:- Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14'''
import datetime
current_date_time = datetime.datetime.now()
current_date = current_date_time.strftime("%d/%m/%Y")
current_time = current_date_time.strftime("%H:%M:%S")
print(f"Current date is {current_date} and time is {current_time}")