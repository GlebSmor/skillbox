first_quarter = int(input('Введите прибыль за первый квартал: '))
second_quarter = int(input('Введите прибыль за второй квартал: '))
third_quarter = int(input('Введите прибыль за третий квартал: '))
fourth_quarter = int(input('Введите прибыль за четвертый квартал: '))
first_half = first_quarter + second_quarter
second_half = third_quarter + fourth_quarter
result = first_half / second_half
print(result)