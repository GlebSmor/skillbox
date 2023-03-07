all_students = []
class_1 = list(range(160, 177, 2))
class_2 = list(range(162, 181, 2))
all_students.extend(class_1)
all_students.extend(class_2)
print('Отсортированный список учеников:', sorted(all_students))
