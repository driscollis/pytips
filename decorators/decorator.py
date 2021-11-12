def info(func):
    def wrapper(*args):
        print('Function name: ' + func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        return func(*args)
    return wrapper

@info
def doubler(number):
    """Doubles the number passed to it"""
    return number * 2

print(doubler(4))