class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


worker1 = Position('Иван', 'Иванов', 'инженер', 1000, 300)
worker2 = Position('Петр', 'Петров', 'дворник', 200, 10)
print(f'Добавлен работник: {worker1.name}, {worker1.surname}, {worker1.position}, {worker1._income}')
print(f'Доход {worker1.get_full_name()} = {worker1.get_total_income()}')
print(f'Добавлен работник: {worker2.name}, {worker2.surname}, {worker2.position}, {worker2._income}')
print(f'Доход {worker2.get_full_name()} = {worker2.get_total_income()}')
