friends = int(input('Кол-во друзей: '))
friends_list = [0] * friends
print(friends_list)
qty_debts = int(input('Долговых расписок: '))
count = 0
for i in range(1, qty_debts + 1):
    print(f'{i}-я расписка')
    to_who = int(input('Кому: '))
    from_who = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[to_who - 1] -= how_much
    friends_list[from_who - 1] += how_much
print('Баланс друзей:')
for i in range(1, len(friends_list) + 1):
    print(f'{i}:', friends_list[i - 1])

