import math
budget = [
  { "name": "John", "age": 28, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]

def get_budgets(value: list) -> float:
    """
    Takes a list of Dictionary of Employees
    and returns the SUM of their budget
    """
    return sum([i['budget'] for i in value])

print("Sum of Employees budget is:", get_budgets(budget))

def avg_year(value:list) -> float:
    """
    Takes a list of Dictionary of Employees
    and returns the AVG of their age
    """
    return sum([i['age'] for i in value])/len(value)

print("Average age of Employees is:", avg_year(budget))