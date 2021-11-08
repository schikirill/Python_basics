src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

"""Решение «в лоб»"""

uniq = []
for element in src:
    if src.count(element) == 1:
        uniq.append(element)
print('uniq_1 = ', uniq)

"""Оптимизация"""

uniq = [element for element in src if src.count(element) == 1]
print('uniq_2 = ', uniq)
