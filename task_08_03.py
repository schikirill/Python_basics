# позиционные аргументы

def type_logger(func):
    def type_arguments(x, y):
        print(f'{x} : {type(x)} , {y} : {type(y)}')
        print(f'Result: {func(x, y)}')
    return type_arguments


@type_logger
def calc_summ(x, y):
    return x + y

calc_summ(10, 5)


@type_logger
def calc_cube(x, y):
    return x ** 3

calc_cube(10, 5)





# именованные аргументы

def type_logger(func):
    def type_arguments(*args):
        print(f'{args} : {type(args)}')
        print(f'Result: {func(*args)}')
    return type_arguments


@type_logger
def calc_summ(x, y):
    return x + y

calc_summ(10, 5)


@type_logger
def calc_cube(x):
    return x ** 3

calc_cube(10)