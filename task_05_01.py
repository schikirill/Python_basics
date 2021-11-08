import sys

"""Генератор нечетных чисел, с использованием yield"""
def odd_number_gen(n):
    for num in range(1, n + 1, 2):
        yield num


odd_numbers = odd_number_gen(18)
print(type(odd_numbers), sys.getsizeof(odd_numbers))  # <class 'generator'> 104
print(next(odd_numbers))    # 1
print(next(odd_numbers))    # 3
print(next(odd_numbers))    # 5
print(next(odd_numbers))    # 7
print(next(odd_numbers))    # 9
print(next(odd_numbers))    # 11
print(next(odd_numbers))    # 13
print(next(odd_numbers))    # 15
print(next(odd_numbers))    # 17
print(next(odd_numbers))    # StopIteration
