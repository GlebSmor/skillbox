def upheaval(number):
    number_2 = 0
    while number > 0:
        remains = number % 10
        number //= 10
        number_2 *= 10
        number_2 += remains
    print('Число наоборот: ', number_2)


while True:
    number = int(input('Введите число: '))
    if number != 0:
        upheaval(abs(number))
    elif number == 0:
        print('Программа завершена!')
        break
