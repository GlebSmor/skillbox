print('Задача 6. Письмо')
side_lenght = int(input('Введите длину стороны письма: '))
letter_square = side_lenght ** 2
square_envelope = 12 ** 2
count = 0
while letter_square > square_envelope:
    letter_square = letter_square / 2
    count += 1
print('Письмо нужно сложить', count, 'раз')
# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
# 
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.