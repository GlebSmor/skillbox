def function(number):
    count = 0
    temp = number
    while temp > 0:
        count += 1
        temp = temp // 10
    last_digit = number % 10
    first_digit = number // 10 ** (count - 1)
    between_digits = number % 10 ** (count - 1) // 10
    number = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    return number


first_n = int(input("Введите первое число: "))
if (first_n / 100) > 1:

    print('Изменённое второе число:', function(first_n))
    second_n = int(input("\nВведите второе число: "))

    if (second_n / 1000) < 1:
        print('Во втором числе меньше четырёх цифр.')

    else:
        print('Изменённое второе число:', function(second_n))
        print('\nСумма чисел:', function(first_n) + function(second_n))

else:
    print('В первом числе меньше трёх цифр.')

