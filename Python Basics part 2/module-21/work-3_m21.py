def fibonacci(num_pos):
    if num_pos == 1 or num_pos == 2:
        return 1
    else:
        return fibonacci(num_pos - 1) + fibonacci(num_pos - 2)


num = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {fibonacci(num)}')
