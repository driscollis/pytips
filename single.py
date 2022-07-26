from functools import singledispatch


@singledispatch
def add(a, b):
    """The generic function"""
    raise NotImplementedError('Unsupported type')


@add.register(int)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


@add.register(float)
def _(a, b):
    print("First argument is of type ", type(a))
    print(a + b)


#add(1, 2)
add(1.0, 2.0)
# add((1,), (2,))
#add([1, 2, 3], [5, 6, 7])