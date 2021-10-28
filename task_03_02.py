def num_translate(numeric):
    ru_en = {
        'ноль': 'zero',
        'один': 'one',
        'два': 'two',
        'три': 'three',
        'четыре': 'four',
        'пять': 'five',
        'шесть': 'six',
        'семь': 'seven',
        'восемь': 'eight',
        'девять': 'nine',
        'десять': 'ten'
    }
    for ru, en in ru_en.items():
        if not numeric.isnumeric():
            if numeric == ru:
                return en
            elif numeric == ru.title():
                return en.title()
            if numeric == en:
                return ru
            elif numeric == en.title():
                return ru.title()


print(num_translate(input('Число от 0 до 10 для перевода (прописью): ')))