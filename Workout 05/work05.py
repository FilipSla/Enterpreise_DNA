list_string = ["Hello", "how", "are", "you?"]

def join_string_v1(value):
    return print(*[i for i in value], sep=" ")

join_string_v1(list_string)

""" 
Problem: Create a function that takes
a list of strings as input. Join each string
in the list to create and return one complete string. Each word should have a space between them.
"""
def join_string_v2(value):
    return " ".join(value)

print(join_string_v2(list_string))