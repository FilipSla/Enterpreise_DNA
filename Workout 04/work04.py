import math

"""
Problem 1: Create a function that takes an angle in radians
and returns the corresponding angle in degrees rounded
to one decimal place.
"""


def radians_to_degrees(value: float) -> float:
    return round(value * 180 / math.pi, 1)


print(radians_to_degrees(20))


"""
Problem 2: Create a function that returns True
when num1 is equal to num2; otherwise return False
"""


def is_same_num(num1, num2):
    return num1 == num2


print(is_same_num(4, 8))
print(is_same_num(2, 2))