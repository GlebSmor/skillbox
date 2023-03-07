family = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Иванов Иван': 44,
    'Иванова Светлана': 38,
    'Воронин Константин': 40,
    'Воронина Вера': 36,
    'Воронина Маша': 8
}
surname = input('Введите фамилию: ').capitalize()

if surname.endswith('а'):
    surname = surname[:len(surname) - 1]

for key, value in family.items():
    if surname in key:
        print(key, value)
        
