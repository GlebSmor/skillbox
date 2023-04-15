N = int(input('Введите кол-во элементов: '))
numbers_list = []
for _ in range(N):
    number = int(input('Введите число: '))
    numbers_list.append(number)
print('Изначальный список:', numbers_list)
print('Отсортированный список:', sorted(numbers_list))

