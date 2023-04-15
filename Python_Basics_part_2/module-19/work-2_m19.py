qty = int(input('Количество стран: '))
towns_data = {}

for num in range(1, qty + 1):
    country = input(f'{num} страна: ').split()
    for town in country[1:]:
        towns_data[town] = country[0]
for num in range(1, 4):
    town = input(f'\n{num} город: ')
    if towns_data.get(town):
        print(f'Город {town} расположен в стране {towns_data.get(town)}.')
    else:
        print(f'По городу {town} данных нет.')



