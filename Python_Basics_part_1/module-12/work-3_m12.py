def kalkulator():
    action = int(input('\nВведите действие 1 - вывести сумму цифр числа 2 - максимальную цифру числа 3 - минимальную цифру числа: '))
    if action == 1:
        summ()
        kalkulator()
    elif action == 2:
        min_n()
        kalkulator()
    elif action == 3:
        max_n()
        kalkulator()
    else:
        print('Ошибка ввода')
        kalkulator()


def summ():
    number = int(input('Введите число: '))
    number_backup = number
    count = 0
    while number != 0:
        count += number % 10
        number //= 10
    print('Сумма цифр числа', number_backup, 'равна', count)


def min_n():
    number = int(input('Введите число: '))
    number_backup = number
    smallest = number % 10
    while number != 0:
        if number % 10 < smallest:
            smallest = number % 10
        number //= 10
    print('Самая маленькая цифра числа', number_backup, 'равна', smallest)


def max_n():
    number = int(input('Введите число: '))
    number_backup = number
    biggest = 0
    while number != 0:
        if number % 10 > biggest:
            biggest = number % 10
        number //= 10
    print('Самая большая цифра числа', number_backup, 'равна', biggest)


#----------------------------------------------------------------------------------------


kalkulator()
