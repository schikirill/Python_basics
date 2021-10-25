list_of_cubes = []
number = int(input("Введите число, до которого необходимо рассчитать: "))
for digit in range(1, number + 1):
    if digit % 2:
        list_of_cubes.append(digit ** 3)

print("Создан список кубов чисел до", digit, '\n', list_of_cubes)
summ_selected_elements = 0
for one_element in list_of_cubes:
    # print("элемент =", one_element)
    temp_variable = one_element
    summ_of_digits = 0
    while temp_variable > 0:
        found_one_digit = temp_variable % 10
        summ_of_digits += found_one_digit
        temp_variable //= 10
    if not summ_of_digits % 7:
        summ_selected_elements += one_element
print("Сумма чисел из списка, сумма цифр которого делится на 7 без остатка:", summ_selected_elements)

# увеличиваем числа из списка на 17

list_of_new_cubes = []
for one_element in list_of_cubes:
    list_of_new_cubes.append(one_element + 17)

print("Создан список из", digit, "чисел из предыдущего списка и увеличенных на 17:"'\n', list_of_new_cubes)
summ_selected_elements = 0
for one_element in list_of_new_cubes:
    temp_variable = one_element
    summ_of_digits = 0
    while temp_variable > 0:
        found_one_digit = temp_variable % 10
        summ_of_digits += found_one_digit
        temp_variable //= 10
    if not summ_of_digits % 7:
        summ_selected_elements += one_element
        print('one_element =', one_element)
print("Сумма чисел из списка (увеличенных на 17), сумма цифр которого делится на 7 без остатка:",
      summ_selected_elements)
