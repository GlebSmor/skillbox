number = int(input('Введите число: '))
number_list = []
for i in range(1, number + 1):
    if i % 2 != 0:
        number_list.append(i)
print('Список из нечётных чисел от одного до N:', number_list)

