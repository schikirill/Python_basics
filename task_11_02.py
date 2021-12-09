class Exception_Class(Exception):
    def __init__(self, error_text):
        self.error_text = error_text

def delenie():
    try:
        delimoe = int(input('Введите делимое: '))
        delitel = int(input('Введите делитель: '))
        if delitel == 0:
            raise Exception_Class("Ошибка! Деление на 0!")
        else:
            print(f'{delimoe} / {delitel} = ', delimoe / delitel)
    except ValueError:
        return print("Вводить можно только цифры")
    except Exception_Class as error:
        return print(error)



delenie()