import random


class KillError(Exception):
    description = 'К сожалению вы умерли =('


class DrunkError(Exception):
    description = 'К сожалению вы спились =('


class CarCrashError(Exception):
    description = 'К сожалению вы попали в аварию =('


class GluttonyError(Exception):
    description = 'К сожалению вы обожрались до смерти =('


class DepressionError(Exception):
    description = 'К сожалению вы умерли от депрессии =('


class Player:

    def __init__(self, name):
        self.name = name
        self.carma = 0
        self.days = 0

    def info(self):
        print(f'Имя: {self.name}\n'
              f'Карма: {self.carma}\n'
              f'Кол-во дней: {self.days}\n')

    def one_day(self):
        self.carma += random.randint(1, 7)
        self.days += 1


error = ''
player = Player(input('Введите имя: '))
while True:
    player.one_day()
    player.info()
    if player.carma == 500:
        print(f'{player.name} достиг просветления!')
        break
    chance = random.randint(1, 10)
    if chance == 10:
        try:
            errors = (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError)
            error = random.choice(errors)
            raise error
        except error:
            print(error.description)
            file = open('karma.log', 'w', encoding='utf-8')
            file.write(str(error) + '\n' + error.description)
            break
