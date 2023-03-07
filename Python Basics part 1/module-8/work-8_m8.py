print('Задача 8. Сумма ряда')
number = int(input('Введите натуральное число: '))
summ = 1
member_line = 1
for summ_line in range(1, number + 1):
    member_line = ((-1) ** summ_line) / (2 ** summ_line)
    summ = member_line + summ
print('Член ряда:', member_line, 'сумма ряда:', summ)
# Дано натуральное число n.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N 
