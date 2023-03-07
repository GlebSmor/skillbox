import random


def play(human):
    if human.satiety < 0:
        print(f'{human.name} умер с голода')
        return True
    num = random.randint(1, 6)
    if human.satiety < 20:
        print(human.eat())
    elif Home.fridge < 10:
        print(human.go_to_market())
    elif Home.locker < 50:
        print(human.work())
    elif num == 1:
        print(human.work())
    elif num == 2:
        print(human.eat())
    else:
        print(human.play())
    return False


class Human:
    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        self.satiety += 1
        Home.fridge -= 1
        return f'{self.name} ест, сытость = {self.satiety}, еда = {Home.fridge}'

    def work(self):
        self.satiety -= 1
        Home.locker += 1
        return f'{self.name} работает, сытость = {self.satiety}, деньги = {Home.locker}'

    def play(self):
        self.satiety -= 1
        return f'{self.name} играет, сытость = {self.satiety}'

    def go_to_market(self):
        Home.fridge += 1
        Home.locker -= 1
        return f'{self.name} идет в магазин, деньги = {Home.locker}, еда = {Home.fridge}'


class Home:
    fridge = 50
    locker = 0


human1 = Human('Вася')
human2 = Human('Петя')

for day in range(1, 366):
    if play(human1) or play(human2):
        print('=(')
        break
    if day == 365:
        print('=)')
