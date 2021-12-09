class Exception_Class(Exception):
    def __init__(self):
        pass

spisok = []
element = 0


def list_numbers():
    print('Введите ЧИСЛА для списка (для остановки введите stop): \n')
    try:
        while 1:
            element = input()
            if str(element).lower() == "stop":
                print(spisok)
                break
            try:
                spisok.append(int(element))
            except ValueError:
                raise Exception_Class
    except Exception_Class:
        print("Ошибка! Не число!")
        list_numbers()


list_numbers()