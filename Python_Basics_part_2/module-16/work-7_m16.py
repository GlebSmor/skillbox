roller_list = []
people_list = []
count = 0
qty_n = int(input('Кол-во коньков: '))
for num in range(1, qty_n + 1):
    size_r = int(input(f'Размер {num}-й пары: '))
    roller_list.append(size_r)

qty_k = int(input('Кол-во людей: '))
for num in range(1, qty_k + 1):
    size_p = int(input(f'Размер ноги {num}-го человека: '))
    people_list.append(size_p)
for foot in sorted(people_list):
    if len(people_list) == 0:
        break
    for size in sorted(roller_list):
        if len(roller_list) == 0:
            break
        if foot <= size:
            count += 1
            roller_list.remove(size)
            people_list.remove(foot)
            break


print('Наибольшее кол-во людей, которые могут взять ролики:', count)

