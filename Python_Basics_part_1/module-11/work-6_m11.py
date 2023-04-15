lower = int(input('Нижняя граница: '))
upper = int(input('Верхняя граница: '))
step = int(input('Шаг: '))
print('C', 'F')
fahrenheit_0 = 32
for degree in range(lower, upper, step):
    if degree == 0:
        print(degree, fahrenheit_0)
    else:
        fahrenheit = float((degree * 1.8) + fahrenheit_0)
        print(degree, int(fahrenheit))
fahrenheit = float((upper * 1.8) + fahrenheit_0)
print(upper, int(fahrenheit))







