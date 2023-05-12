'''Write a Python program to compute the future value of a
specified principal amount, rate of interest, and number of years'''
amount = eval(input("Enter the amount in rupees :- "))
rate_of_interest = eval(input("Enter the rate of percentage :- "))
no_of_years = int(input("Enter the no of years :- "))
def total_amount_cal (p,r,t):
    total_amount = p*(1+(0.01*r))**t
    return total_amount
final_amount = total_amount_cal(amount,rate_of_interest,no_of_years)
print(f"The Future value of principal amount - {amount} with rate of interest - {rate_of_interest} "
      f"for {no_of_years} years is {final_amount} ")


