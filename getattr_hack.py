# Works in Python 3.7+

def __getattr__(expression):
    operator, number = expression.split("_")
    number = int(number)
    operations = {"times": lambda val: val * number}
    if operator not in operations:
        print(f"Unknown operator: {operator}")
        return print
    return operations[operator]
