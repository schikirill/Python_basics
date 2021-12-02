class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки оригинальный')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(f'Запуск отрисовки ручка\n')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(f'Запуск отрисовки карандаш\n')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(f'Запуск отрисовки маркер\n')


Pen = Pen('Берем ручку')
Pen.draw()

Pencil = Pencil('Берем карандаш')
Pencil.draw()

Handle = Handle('Берем маркер')
Handle.draw()