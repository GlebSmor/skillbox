players_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
count = 0
for players in players_list:
    if count % 2 == 0:
        first_day.append(players_list[count])
    count += 1
print('Первый день:', first_day)
