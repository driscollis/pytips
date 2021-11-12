class decorator_with_arguments:

    def __init__(self, arg1, arg2):
        print('in __init__')
        self.arg1 = arg1
        self.arg2 = arg2
        print('Decorator args: {}, {}'.format(arg1, arg2))

    def __call__(self, f):
        print('in __call__')
        def wrapped(*args, **kwargs):
            print('in wrapped()')
            return f(*args, **kwargs)
        return wrapped

@decorator_with_arguments(3, 'Python')
def doubler(number):
    return number * 2

print(doubler(5))