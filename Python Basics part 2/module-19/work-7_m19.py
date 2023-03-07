qty = int(input('Введите количество заказов: '))
pizza_dict = {}


for num in range(1, qty + 1):
    order = input(f'{num} заказ: ')
    fio, pizza, amount = order.split(maxsplit=3)
    amount = int(amount)
    if fio not in pizza_dict:
        pizza_dict[fio] = {pizza: amount}
    else:
        if pizza not in pizza_dict[fio]:
            pizza_dict[fio][pizza] = amount
        else:
            pizza_dict[fio][pizza] += amount
for fio, order in sorted(pizza_dict.items()):
    print(f'{fio}:')
    for pizza, amount in sorted(order.items()):
        print('\t', pizza, amount)
