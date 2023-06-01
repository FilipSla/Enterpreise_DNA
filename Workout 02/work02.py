from datetime import datetime

"""Problem 1: Create a function that takes two arguments:
the original price and the discount percentage as integers 
and returns the final price after the discount."""
def final_price(discount, price):
    return price * (1 - discount / 100)


print(final_price(10, 20))

"""
Problem 2: Create a function that takes the age
in years and returns the age in days.
"""
def calc_age(years):
    return years * 365.25


print(calc_age(66.66))


"""
Problem 3: Create a function, get_days,
that takes two dates and returns the number of days
between the first and second date
"""
def get_days(day1, day2):
    day1 = datetime.strptime(day1, "%m-%d-%Y")
    day2 = datetime.strptime(day2, "%m-%d-%Y")
    return abs((day2 - day1).days)

print(get_days("05-12-1978", "05-08-2022"))