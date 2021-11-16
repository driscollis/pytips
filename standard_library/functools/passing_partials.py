from functools import partial


def add(x, y):
    """"""
    return x + y


def multiply(x, y):
    return x * y


def run(func):
    """
    Run a partial function
    """
    print(func())


def main():
    a1 = partial(add, 1, 2)
    m1 = partial(multiply, 5, 8)
    run(a1)
    run(m1)

if __name__ == "__main__":
    main()