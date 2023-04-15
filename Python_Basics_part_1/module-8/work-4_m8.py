print('Задача 4. Отрезок')
number_a = int(input('Введите число а: '))
number_b = int(input('Введите число b: '))
number_c = int(input('Введите число c: '))

arithmetic_mean = 0
count = 0
for segment in range(number_a, number_b + 1):
    if segment % number_c == 0:
        arithmetic_mean += segment
        count += 1
arithmetic_mean = arithmetic_mean / count
print('Cреднее арифметическое всех чисел из отрезка [a; b], кратных числу c =', arithmetic_mean)
#Напишите программу, 
# которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).