""" 
Problem: Create a function that takes a list
of non-negative integers and strings and return
a new list without the strings.
"""


def filter_list(value: list) -> list:
    return [i for i in value if type(i) == int and i >= 0]


print(filter_list([1, -2, "a", "b"]))
print(filter_list([1, "a", "b", 0, 15]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
