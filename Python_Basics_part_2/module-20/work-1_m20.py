students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def function(x_dict):
    interests = []
    full_len = 0
    for ind, val in x_dict.items():
        interests.extend(val['interests'])
        full_len += len(val['surname'])
    return set(interests), full_len


pairs = []
for index, value in students.items():
    pairs.append((index, value['age']))


print(f'Список пар "ID студента — возраст": {pairs}')

students_interests, surname_full_len = function(students)
print(f'Полный список интересов всех студентов: {students_interests}'
      f'\nОбщая длина всех фамилий студентов: {surname_full_len}')