list_of_prices = [0.30, 0.01, 74.4, 11.0, 42.91, 17, 4.31, 50.15, 67.97, 83.78, 72.1, 94.02, 88.30, 82.91, 32.41, 16.3, 8.4, 98.1, 97.83, 17.76]
readable_prices = []
for element in list_of_prices:
    fix_price = str(element)
    fix_price = str(fix_price).split('.')
    if len(fix_price) > 1:
        if len(fix_price[1]) == 1 and int(fix_price[1]) != 0:
            readable_prices.append(f'{int(fix_price[0]):0d} руб {int(fix_price[1]) * 10:.0f} коп')
        else:
            if int(fix_price[1]) == 0:
                readable_prices.append(f'{int(fix_price[0]):0d} руб 0{fix_price[1]} коп')
            else:
                if len(fix_price[1]) > 1 and int(fix_price[1]) <= 9:
                    readable_prices.append(f'{int(fix_price[0]):0d} руб {fix_price[1]} коп')
                else:
                    readable_prices.append(f'{int(fix_price[0]):0d} руб {int(fix_price[1]):.0f} коп')
    else: readable_prices.append(f'{int(fix_price[0]):0d} руб 00 коп')
print(f'Список обработанных цен:', readable_prices)

# сортировка по возрастанию, без создания нового объекта
list_of_prices = [0.30, 0.01, 74.4, 11.9, 42.91, 17, 4.31, 50.15, 67.97, 83.78, 72.1, 94.02, 88.30, 82.91, 32.41, 16.3, 8.4, 98.1, 97.83, 17.76]
print(f'Начальный список:', list_of_prices, 'и его ID:', id(list_of_prices))
list_of_prices.sort()
print(f'По возрастанию:', list_of_prices, 'и его ID:', id(list_of_prices))


# сортировка по убыванию. Новый объект
list_of_prices = [0.30, 0.01, 74.4, 11.9, 42.91, 17, 4.31, 50.15, 67.97, 83.78, 72.1, 94.02, 88.30, 82.91, 32.41, 16.3, 8.4, 98.1, 97.83, 17.76]
print(f'Начальный список:', list_of_prices, 'и его ID:', id(list_of_prices))
list_of_prices = sorted(list_of_prices, reverse=True)
print(f'По убыванию:', list_of_prices, 'и его ID:', id(list_of_prices))

# вывод цены пяти самых дорогих товаров
list_of_prices = [0.30, 0.01, 74.4, 11.9, 42.91, 17, 4.31, 50.15, 67.97, 83.78, 72.1, 94.02, 88.30, 82.91, 32.41, 16.3, 8.4, 98.1, 97.83, 17.76]
print(f'5 самых дорогих товаров по возрастанию цены:', sorted(list_of_prices, reverse=True)[:5][::-1])