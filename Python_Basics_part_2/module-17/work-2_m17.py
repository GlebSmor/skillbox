long = int(input('Введите длину списка: '))
output_list = [(1 if x % 2 == 0 else x % 5) for x in range(long)]
print(output_list)
