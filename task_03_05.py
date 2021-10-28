from random import choice


def get_jokes(how_many):
    """Генерирует шутки из готовых списков, по одному слову из каждого списка"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    count = int(how_many)
    while count > 0:
        print([choice(nouns)] + [choice(adverbs)] + [choice(adjectives)])
        count -= 1


get_jokes(how_many = input("Сколько шуток выдать? "))