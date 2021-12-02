class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        print(f'\n{self.color.capitalize()} машина {self.name} поехала')

    def stop(self):
        print(f'{self.color.capitalize()} машина {self.name} остановилась')

    def turn(self):
        import random
        direction = random.choice(['налево', 'направо'])
        print(f'{self.color.capitalize()} машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name} = {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'! Превышение допустимой скорости на {self.speed - 60} км/ч для {self.name} !')


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'! Превышение допустимой скорости на {self.speed - 40} км/ч для {self.name} !')


class SportCar(Car):
    def show_speed(self):
        super().show_speed()
        print(f'! Для {self.name} скорость неограничена !')


class PoliceCar(Car):
    def show_speed(self):
        self.is_police = True
        super().show_speed()
        if self.is_police == True:
            print(f'! {self.name} виу-виу-виу-кря-кря !')
            


TownCar = TownCar('TownCar', 90, 'черный')
TownCar.go()
TownCar.turn()
TownCar.show_speed()
TownCar.turn()
TownCar.stop()

WorkCar = WorkCar('WorkCar', 30, 'белый')
WorkCar.go()
WorkCar.turn()
WorkCar.show_speed()
WorkCar.turn()
WorkCar.stop()

PoliceCar = PoliceCar('PoliceCar', 150, 'бело-красно-белый')
PoliceCar.go()
PoliceCar.turn()
PoliceCar.show_speed()
PoliceCar.turn()
PoliceCar.stop()