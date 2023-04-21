'''Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)'''
from datetime import date
date_1 = date(2014, 7, 2)
date_2 = date(2014, 7, 11)
difference = date_2-date_1
print(f"The Difference between {date_1} and {date_2} is {difference.days} days")