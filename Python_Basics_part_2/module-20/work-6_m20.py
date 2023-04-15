import random

original_list = [random.randint(0, 100) for _ in range(10)]
changed_list = [(original_list[index], original_list[index + 1])
                for index, value in enumerate(original_list) if index % 2 == 0]
# changed_list = [(original_list[index], original_list[index + 1])
#                 for index in range(0, len(original_list) - 1) if index % 2 == 0]
print(f'Оригинальный список: {original_list}')
print(f'Новый список: {changed_list}')
