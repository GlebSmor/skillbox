def annuity(k, p):
    t = pow(p + 1, k)
    return p * t / (t - 1)


def print_info(j, s, i):
    print(f'\nПериод:', round(j, 2))
    print(f'Остаток долга на начало периода:', round(s, 2))
    print(f'Выплачено процентов:', round(s * i, 2))
    ds = a - s * i
    print(f'Выплачено тела кредита:', round(ds, 2))
    return s - ds


s = float(input('Введите сумму кредита: '))
n = int(input('На сколько лет выдан? '))
i = float(input('Сколько процентов годовых? ')) / 100

a = s * annuity(n, i)
for j in range(1, 4):
    s = print_info(j, s, i)

print(f'\nОстаток долга:', round(s, 2))
print('\n==============================\n')

n2 = int(input('На сколько лет продляется договор? '))
i2 = float(input('Увеличение ставки до: ')) / 100
n = n2 + n - 3

a = s * annuity(n, i2)
for j in range(1, n + 1):
    s = print_info(j, s, i2)

print(f'\nОстаток долга:', round(s, 2))
