
def reverse(number):
    number_2 = 0
    while number > 0:
        remains = number % 10
        number //= 10
        number_2 *= 10
        number_2 += remains
    return number_2


number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
print('Первое число наоборот:', reverse(number_1))
print('Второе число наоборот:', reverse(number_2))
summa = reverse(number_1) + reverse(number_2)
print('Сумма:', summa)
print('Сумма наоборот:', reverse(summa))


