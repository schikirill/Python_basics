def val_checker(func):
    def wrapped(x):
        if not x > 0:
            raise ValueError(f'wrong value: {x}')
        else:
            print(f'Result: {func(x)}')

    return wrapped


@val_checker
def calc_cube(x):
    return x ** 3


calc_cube(5)
calc_cube(-5)
