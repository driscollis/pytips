from functools import wraps


def another_function(func):
    """
    A function that accepts another function
    """

    @wraps(func)
    def wrapper():
        """
        A wrapping function
        """
        val = f"The result of {func()} is {eval(func())}"
        return val
    return wrapper


@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"


if __name__ == "__main__":
    print(a_function.__name__)
    print(a_function.__doc__)