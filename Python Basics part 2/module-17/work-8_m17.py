import random
output = ''
sticks = int(input('Количество палок: '))
sticks_list = [i for i in range(1, sticks + 1)]
throws_list = int(input('Количество бросков: '))

for throw in range(throws_list):
    L = random.randint(1, sticks)
    R = random.randint(L, sticks)
    print(f'Бросок {throw + 1} Сбиты палки с номера', L, 'по номер', R, '.')

    for num in range(L - 1, R):
        sticks_list[num] = '.'


for sym in range(len(sticks_list)):
    if sticks_list[sym] != '.':
        sticks_list[sym] = '|'

for sym in sticks_list:
    output += sym

print('\nРезультат:', output)