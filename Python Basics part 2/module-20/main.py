def score_key(a):
    return a[1][0]*100000000 - a[1][1]


score_table = {}
qty = int(input('Сколько записей вносится в протокол? '))

for time in range(1, qty + 1):
    ball, name = input(f'{time}-я запись: ').split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]

scores = list(score_table.items())
scores.sort(key=score_key, reverse=True)
print('\nИтоги соревнований:')
for place in range(1, 4):
    print(f'{place}-е место. {scores[place - 1][0]} ({scores[place - 1][1][0]})')
