qty = int(input('Количество клеток: '))
cells_list = []
output = []
for cell_number in range(1, qty + 1):
    cell = int(input(f'Эффективность {cell_number} клетки: '))
    cells_list.append(cell)
for number in range(len(cells_list)):
    if cells_list[number] < number:
        output.append(cells_list[number])
