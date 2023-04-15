class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potato.states[self.state]}')


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает! ')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка еще не созрела!\n')
        else:
            print('Вся картошка созрела. Можно собирать\n')


class Gardener:
    def __init__(self, name, collected_potatoes):
        self.name = name
        self.collected_potatoes = collected_potatoes

    def gardener_info(self):
        print(f'Имя садовника: {self.name}\nСколько собрал картошки: {self.collected_potatoes}\n')

    def tend(worker, my_garden):
        while True:
            if all([i_potato.is_ripe() for i_potato in my_garden.potatoes]):
                question = int(input('Собрать картошку? \n1 - да\n2 - нет\n'))
                if question == 1:
                    potato_count = 0
                    for i_potato in my_garden.potatoes:
                        worker.collected_potatoes += 1
                        potato_count += 1
                    i_potato.state = 0

                    print(f'{worker.name} собрал {potato_count} картофелин!')
                    worker.gardener_info()
                    break

                else:
                    print('Прошло некоторое время\n')

            else:
                question = int(input(f'Отправить {worker.name} ухаживать за картошкой? \n1 - да\n2 - нет\n'))
                if question == 1:
                    my_garden.grow_all()
                    my_garden.are_all_ripe()
                else:
                    print("Прошло некоторое время\n")


my_garden = PotatoGarden(5)
worker = Gardener('Садовник', 0)
Gardener.tend(worker, my_garden)
