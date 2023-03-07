first_list = []
second_list = []
for num in range(1, 4):
    number = int(input(f'Введите {num}-е число для первого списка: '))
    first_list.append(number)
print()
for num in range(1, 8):
    number = int(input(f'Введите {num}-е число для второго списка: '))
    second_list.append(number)
print('\nПервый список:', first_list, '\nВторой список:', second_list)
first_list.extend(second_list)

for element in first_list[:]:
    for _ in range(first_list.count(element) - 1):
        first_list.remove(element)

print('Новый первый список с уникальными элементами:', first_list)