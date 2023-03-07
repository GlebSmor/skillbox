size = int(input('Укажите размер файла для скачивания: '))
speed = int(input('Какова скорость вашего соединения? '))
seconds = 1
for mb in range(speed, size, speed):
    print('Прошло', seconds, 'сек.', 'Скачано', mb, 'из', size, 'МБ')
    seconds += 1
else:
    print('Прошло', seconds, 'сек.', 'Скачано', size, 'из', size, 'МБ')








