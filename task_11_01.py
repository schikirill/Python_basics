import datetime

class Data:
    def __init__(self, data):
        self.data = data.split(sep='-')

    @classmethod
    def convert_data(cls, date):
        try:
            for element in date.split(sep='-'):
                print(f'Класс {type(int(element))}, число {int(element)}')
        except ValueError:
            print(f'Неправильная дата! Ошибка в {element}!')

    @staticmethod
    def validate_data(date):
        try:
            day, month, year = date.split(sep='-')
            datetime.date(int(year), int(month), int(day))
            print(f'правильная дата!')
        except ValueError:
            print(f'Неправильная дата!')




Data.convert_data('07-12-2021')
Data.validate_data('07-12-2021')
Data.convert_data('O7-12-2021')
Data.validate_data('O7-12-2021')
Data.convert_data('07-13-2021')
Data.validate_data('07-13-2021')

