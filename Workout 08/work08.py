"""
Factorial 
"""


def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


""" 
Write a function that takes a list of numbers and returns a list with two elements:

The first element should be the sum of all even numbers in the list.
The second element should be the sum of all odd numbers in the list.

"""

# List comprehension method
def sum_odd_and_even(value: list) -> list:
    even_sum = sum([i for i in value if i % 2 == 0])
    odd_sum = sum([i for i in value if i % 2 == 1])
    return [even_sum, odd_sum]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))