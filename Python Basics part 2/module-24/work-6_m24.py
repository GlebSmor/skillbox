class Water:
    name = 'Вода'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Dirt()
        elif other.name == Water.name:
            return Water()


class Air:
    name = 'Воздух'

    def __add__(self, other):
        if other.name == 'Вода':
            return Storm()
        elif other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Земля':
            return Dust()
        elif other.name == Air.name:
            return Air()


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Вода':
            return Steam()
        elif other.name == 'Земля':
            return Lava()
        elif other.name == Fire.name:
            return Fire()


class Earth:
    name = 'Земля'

    def __add__(self, other):
        if other.name == 'Воздух':
            return Dust()
        elif other.name == 'Огонь':
            return Lava()
        elif other.name == 'Вода':
            return Dirt()
        elif other.name == Earth.name:
            return Earth()


class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Dirt:
    name = 'Грязь'


class Lightning:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


elements = {1: Water(), 2: Air(), 3: Fire(), 4: Earth()}
while True:
    try:
        element_1 = elements[int(input('Выберите 1 элемент:\n'
                                       '1 - Вода\n'
                                       '2 - Воздух\n'
                                       '3 - Огонь\n'
                                       '4 - Земля\n'))]

        element_2 = elements[int(input('Выберите 2 элемент:\n'
                                       '1 - Вода\n'
                                       '2 - Воздух\n'
                                       '3 - Огонь\n'
                                       '4 - Земля\n'))]
        result = element_1 + element_2
        print(f'{element_1.name} + {element_2.name} = {result.name}')
        break
    except KeyError:
        print('\nВведен элемент не из списка!\n')
        