import random


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.ashed = 0
        self.cat_food = 30

    def __str__(self):
        return f'В доме денег: {self.money}, еды: {self.food}, кошачья еда: {self.cat_food}, грязи: {self.ashed}'


class Human:

    def __init__(self):
        self.fullness = 30
        self.happiness = 100
        self.house = home

    def __str__(self):
        return f'еда: {self.fullness}, счастье {self.happiness}'

    def depression(self):
        if self.house.ashed >= 90:
            self.happiness -= 5

    def hungry(self):
        self.fullness -= 10


class Husband(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):

        if (self.fullness <= 0) or (self.happiness <= 0):
            print(f'{self.name} умер...')
            return

        super().depression()
        super().hungry()

        dice = random.randint(1, 4)

        if self.house.money < 70:
            self.work()
        elif self.happiness < 30:
            self.gaming()
        elif self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.work()
        elif dice == 4:
            self.pet_the_cat()

    def pet_the_cat(self):

        if self.fullness < 20:
            self.eat()
            return

        elif alice.happiness < 30:
            self.work()
            return

        else:
            self.happiness += 5
            print(f'{self.name} гладил кота')
            return

    def eat(self):

        if self.fullness > 40:
            self.work()
        elif self.fullness > 30:
            self.gaming()
        elif self.house.food > 20:
            self.fullness += 20
            self.house.food -= 20
            print(f'{self.name} поел, теперь eго сытость:{self.fullness}')
        elif self.house.food < 30:
            print(
                f'{self.name} пытался поесть, но дома нет еды... Он расстроился и его счастье уменьшилось '
                f'до {self.happiness}')

    def work(self):
        if self.fullness < 30:
            self.eat()
        else:
            self.fullness -= 10
            self.house.money += 200
            self.happiness += 10
            print(
                f'{self.name} заработал 150 крышек, теперь денег дома:{self.house.money} '
                f'он рад что все идет хорошо и его счастье вырастает до {self.happiness}')

    def gaming(self):
        if self.happiness > 40:
            self.act()
        elif self.fullness < 20:
            self.eat()
        elif alice.happiness < 30:
            self.work()
        else:
            self.happiness += 30
            print(f'{self.name} заигрался в танки, зато теперь его счастье:{self.happiness}')


class Wife(Human):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}, счастье {self.happiness}'

    def act(self):

        if (self.fullness <= 0) or (self.happiness <= 0):
            print('{} умерла...'.format(self.name))

        super().depression()
        super().hungry()

        dice = random.randint(1, 5)

        if self.house.food < 60:
            self.shopping()
        elif self.happiness < 30:
            self.buy_fur_coat()
        elif self.fullness < 40:
            self.eat()
        elif self.happiness < 30:
            self.buy_fur_coat()
        elif self.house.ashed > 70:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.clean_house()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.buy_fur_coat()
        elif dice == 5:
            self.pet_the_cat()

    def pet_the_cat(self):

        if self.fullness < 20:
            self.eat()

        elif self.happiness > 100:
            self.clean_house()

        elif self.happiness > 5:
            print(f'{self.name} гладила кота')

    def eat(self):

        eat_count = random.randint(20, 30)

        if self.fullness > 40:
            self.shopping()

        elif self.house.food < 30:
            self.shopping()

        elif self.house.food > eat_count:
            self.fullness += eat_count
            self.house.food -= eat_count
            print(f'{self.name} поелa, теперь ee сытость:{self.fullness}')

        else:
            self.happiness -= 10
            print(
                f'{self.name} пыталась поесть, но дома нет еды... Она расстроилась и ее счастье уменьшилось '
                f'до {self.happiness}')

    def shopping(self):
        food_count = random.randint(30, 60)
        cat_food_count = random.randint(10, 20)

        if self.house.money > 400:
            food_count *= 3
            cat_food_count *= 2

        elif self.house.money > 250:
            food_count *= 2
            cat_food_count *= 2

        if (self.fullness < 20) and (self.house.food > 30):
            self.eat()

        elif self.house.food > 100:
            self.act()

        elif self.house.money <= food_count + cat_food_count:
            print(f'{self.name} хотела пойти в магазин, но деньги кончились')
            self.clean_house()

        elif (self.house.cat_food < 40) or (self.house.cat_food < 20):
            self.house.food += food_count
            self.house.cat_food += cat_food_count
            self.house.money -= cat_food_count + food_count
            self.happiness += 10

            print(f'{self.name} закупилась продуктами, теперь в холодильнике:{self.house.food}'
                  f',а так же захватила кошачью еду, теперь ее:{self.house.cat_food}, '
                  f'она рада что все хорошо и ее радость выросла до {self.happiness}')

        else:
            self.house.food += food_count
            self.house.money -= food_count
            self.happiness += 10
            print(f'{self.name} закупилась продуктами, теперь в холодильнике:{self.house.food}'
                  f', она рада что все хорошо и ее радость выросла до {self.happiness}')

    def buy_fur_coat(self):

        if self.house.money > 400:
            self.house.money -= 350
            self.happiness += 60
            print(f'{self.name} очень рада что купила шубу, теперь ее счастье:{self.happiness}')
            return

        elif self.house.money < 400:
            print(f'{self.name} очень хотела шубу, но у них пока нет денег на нее')
            self.pet_the_cat()

        elif self.happiness > 100:
            self.clean_house()

    def clean_house(self):

        if self.house.ashed > 90:
            self.house.ashed -= 100
            print(
                f'{self.name} весь день убиралась, зато теперь дома дома чище и ее счастье выросло до {self.happiness}')

        elif self.house.ashed < 90:
            self.act()


class Cat:

    def __init__(self, name):
        self.house = home
        self.name = name
        self.fullness = 30

    def __str__(self):
        return f'{self.name}: сытость: {self.fullness}'

    def hungry(self):
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} умер от голода')
            return

        self.hungry()

        dice = random.randint(1, 3)

        if self.fullness < 30:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        elif dice == 3:
            self.soil()

    def eat(self):
        eat_count = random.randint(5, 10)
        if self.house.cat_food > eat_count:
            self.house.cat_food -= eat_count
            self.fullness += eat_count * 2
            print(f'{self.name} поела, теперь ее сытость: {self.fullness}')
        else:
            print(f'{self.name} пыталась покушать, но кошачья еда кончилась')

    def sleep(self):
        print(f'{self.name} спала весь день')

    def soil(self):
        self.house.ashed -= 5
        print(f'{self.name} заигралась с обоями, грязь в доме увеличилась до: {self.house.ashed}')


home = House()
serge = Husband(name='Сережа')
alice = Wife(name='Алиса')
cat = Cat(name='Рыжик')

for day in range(1, 366):
    print(f'================== День {day} ==================')
    serge.act()
    alice.act()
    cat.act()
    print(cat)
    print(serge)
    print(alice)
    print(home)
    home.ashed += 5
