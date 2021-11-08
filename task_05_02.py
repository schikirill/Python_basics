import sys

"""Генерация нечетных чисел, без использования yield"""

n = int(input('What number? \n'))
odd_number_gen = (num for num in range(1, n + 1, 2))
print(*odd_number_gen, sep='\n')

print(type(odd_number_gen), sys.getsizeof(odd_number_gen))  # <class 'generator'> 104