import random


class Warrior:
    def __init__(self, health, name):
        self.health = health
        self.name = name


warrior1 = Warrior(100, 'Ogre')
warrior2 = Warrior(100, 'Knight')
while warrior1.health > 0 and warrior2.health > 0:
    get_damage = random.randint(1, 2)
    if get_damage == 1:
        warrior1.health = warrior1.health - 20
        print(f'{warrior2.name} нанес удар {warrior1.name}\n'
              f'{warrior2.name} == {warrior2.health} HP\n'
              f'{warrior1.name} == {warrior1.health} HP\n')
    else:
        warrior2.health = warrior2.health - 20
        print(f'{warrior1.name} нанес удар {warrior2.name}\n'
              f'{warrior1.name} == {warrior1.health} HP\n'
              f'{warrior2.name} == {warrior2.health} HP\n')

