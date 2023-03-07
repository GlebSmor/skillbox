n = int(input('Количество контейнеров: '))
container_list = []
for _ in range(n):
    while True:
        weight = int(input('Введите вес контейнера: '))
        if weight <= 200:
            break
        else:
            print('Ошибка! Вес контейнера не должен превышать 200')

    container_list.append(weight)
while True:
    new_container = int(input('\nВведите вес нового контейнера: '))
    if new_container <= 200:
        break
    else:
        print('Ошибка! Вес контейнера не должен превышать 200')
count = 1
for num in container_list:
    if num >= new_container:
        count += 1
print(count)
