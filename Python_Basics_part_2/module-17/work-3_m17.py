import random
team_1 = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
team_2 = [round(random.uniform(5.00, 10.00), 2) for _ in range(20)]
winners = []
for player in range(len(team_1)):
    if team_1[player] > team_2[player]:
        winners.append(team_1[player])
    else:
        winners.append(team_2[player])

print('Первая команда:', team_1)
print('Вторая команда:', team_2)
print('Победители тура:', winners)
