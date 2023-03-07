import random
qty = int(input('Количество чисел в списке: '))
list_main = [random.randint(0, 2) for _ in range(qty)]
compress = [x for x in list_main if x > 0]
print('Список до сжатия:', list_main)
print('Список после сжатия:', compress)
