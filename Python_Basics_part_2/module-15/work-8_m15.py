N = int(input('Введите кол-во элементов: '))
numbers_list = []

for _ in range(N):
    number = int(input('Введите число: '))
    numbers_list.append(number)

K = int(input('Сдвиг: '))
print('Изначальный список: ', numbers_list)
new_numbers_list = numbers_list[-K:] + numbers_list[:-K]
print(new_numbers_list)
