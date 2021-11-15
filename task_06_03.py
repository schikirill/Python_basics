import sys

with open('users.csv', 'r', encoding='utf-8') as u:
    dict_key = u.read().replace(",", " ").splitlines()
with open('hobby_15.csv', 'r', encoding='utf-8') as h:
# при использовании 'hobby_15.csv' добавляется 'None', при использовании 'hobby_32.csv' - выход с кодом "1"
    dict_value = h.read().splitlines()

if len(dict_key) > len(dict_value):
    while len(dict_key) > len(dict_value):
        dict_value.append('None')
    hobby_dict = dict(zip(dict_key, dict_value))
    print(hobby_dict)
else:
    sys.exit("Выход из скрипта с кодом «1»")

# Запись в новый файл (не выполняется, если выход с кодом 1)

with open('hobby_dict.txt', 'w') as hd:
    hd.write(str(hobby_dict))

# Проверка

with open('hobby_dict.txt', 'r') as hd:
    print(f"Читаем файл {hd.name}: {hd.read()}")