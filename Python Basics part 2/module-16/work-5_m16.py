violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
time = 0
qty = int(input('Сколько песен выбрать? '))
for num in range(1, qty + 1):
    name = input(f'Название {num}-й песни: ')
    for track in range(len(violator_songs)):
        if violator_songs[track][0] == name:
            time += violator_songs[track][1]

print('\nОбщее время звучания песен:', round(time, 2))
