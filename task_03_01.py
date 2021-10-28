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


def num_translate(numeric):
    for ru, en in ru_en.items():
        if not numeric.isnumeric():
            if numeric == ru:
                return en
            if numeric == en:
                return ru


print(num_translate(input('Число от 0 до 10 для перевода (прописью): ')))