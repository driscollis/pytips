from functools import partial

def add(x, y):
    return a + b

if __name__ == "__main__":
    p_add = partial(add, 2)
    print(p_add(4))