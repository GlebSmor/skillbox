number_people = int(input('Введите количество человек: '))
data_dict = dict()
level_dict = dict()

for i in range(1, number_people):
    descendant_name, parent_name = input(f'{i} пара: ').split()
    data_dict[descendant_name] = parent_name
    level_dict[descendant_name] = 0
    level_dict[parent_name] = 0

for i in data_dict:
    people = i
    while people in data_dict:
        people = data_dict[people]
        level_dict[i] += 1

print('\n“Высота” каждого члена семьи:')
for i in sorted(level_dict):
    print(i, level_dict[i])

