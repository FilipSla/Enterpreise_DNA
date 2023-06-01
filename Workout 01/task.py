def convert(number: int | float) -> int | float:
    """convert function "Minutes to seconds"

    Args:
        number (int | float): Minutes

    Raises:
        TypeError: Input must be int or float

    Returns:
        int|float: Converted number into seconds
    """
    if not all([isinstance(i, int | float) for i in [number]]):
        raise TypeError("Input must be int or float!")
    else:
        return number * 60


print(convert(22.25))


def make_sum(num1: int | float, num2: int | float) -> int | float:
    """make_sum Function that sum two numbers

    Args:
        num1 (int | float): First number
        num2 (int | float): Second number

    Raises:
        TypeError: Inputs must be int or float!

    Returns:
        int | float: Sum of two numbers
    """
    if not all([isinstance(i, int | float) for i in [num1, num2]]):
        raise TypeError("Inputs must be int or float!")
    else:
        return num1 + num2


print(make_sum(44, 57.4))


def fizz_buzz(num: int | float) -> str:
    """fizz_buzz Fizz buzz interview task

    Args:
        num (int | float): Number

    Raises:
        TypeError: Input must be int or float

    Returns:
        ans (str): Solution
    """
    if not all([isinstance(i, int | float) for i in [num]]):
        raise TypeError("Input must be int or float!")
    if num % 3 == 0 and num % 5 == 0:
        ans = "FizzBuzz"
    elif num % 3 == 0:
        ans = "Fizz"
    elif num % 5 == 0:
        ans = "Buzz"
    return ans

print(fizz_buzz(155))