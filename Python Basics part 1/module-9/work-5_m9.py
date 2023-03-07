x_axis = 8
y_axis = 10
print('Введите команду: север (клавиша W), юг (клавиша S), запад (клавиша A), восток (клавиша D), для выхода введите Stop')
while True:
    print('[Программа]: Марсоход находится на позиции', x_axis, y_axis,)
    operator = input('[Оператор]: ')
    if operator == 'W' or operator == 'w' and 0 <= y_axis < 20:
        y_axis += 1
    if operator == 'S' or operator == 's' and 0 < y_axis <= 20:
        y_axis -= 1
    if operator == 'A' or operator == 'a' and 0 < x_axis <= 15:
        x_axis -= 1
    if operator == 'D' or operator == 'd' and 0 <= x_axis < 15:
        x_axis += 1
    if operator == 'Stop' or operator == 'stop':
        break
print('Тестирование окончено, cпасибо!')


