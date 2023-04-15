import math


class Car:
    def __init__(self, corner, x=0, y=0):
        self.x = x
        self.y = y
        self.corner = corner

    def __str__(self):
        return f'Автомобиль находится в точкe (x == {self.x}, y == {self.y}'

    def move(self, dist):
        self.x += dist * math.cos(self.corner)
        self.y += dist * math.sin(self.corner)

    def turn(self, new_corner):
        self.corner = new_corner


class Bus(Car):
    max_passengers = 40
    pay_coef = 0.1

    def __init__(self, corner):
        super().__init__(corner)
        self.passengers = 0
        self.money = 0

    def __str__(self):
        return super().__str__() + f'\nКол-во пассажиров: {self.passengers}\n' \
                                   f'Денег заработано: {self.money}'

    def move(self, dist):
        self.money = Bus.pay_coef * self.passengers * dist
        super().move(dist)

    def turn(self, new_corner):
        self.corner = new_corner

    def passenger_in(self, qty_in):
        if self.passengers + qty_in < self.max_passengers:
            self.passengers += qty_in
        else:
            qty_in = qty_in - ((self.passengers + qty_in) - self.max_passengers)
            self.passengers += qty_in
            print('Достигнуто максимальное кол-во пассажиров')

    def passenger_out(self, qty_out):
        if self.passengers > 0:
            self.passengers -= qty_out
        else:
            print('Автобус пустой')

