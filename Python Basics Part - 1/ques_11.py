''' Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).'''
fn_name = input("Enter the Function name without ():-")
fn_name=eval(fn_name)
print(f"Function Description :- {fn_name.__doc__}")