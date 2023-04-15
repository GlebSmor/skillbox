class Student:

    def __init__(self, name, group_num, scores_list):
        self.fi = name
        self.gr_num = group_num
        self.scores_list = scores_list
        average_sc = 0
        count = 0
        for score in scores_list:
            average_sc += score
            count += 1
        self.average_sc = average_sc / count

    def info(self):
        self.scores_list = [str(x) for x in self.scores_list]
        print(f'\nФИ: {self.fi}\n'
              f'Номер группы: {self.gr_num}\n'
              f'Cписок оценок: {" ".join(self.scores_list)}\n'
              f'Средний балл: {self.average_sc}')


students_list = []
for _ in range(1, 11):
    fi, gr_num = input('Введите ФИ, Номер группы (через запятую): ').split(',')
    grade_list = input('Введите список из 5 оценок (через пробел): ').split(maxsplit=4)
    grade_list = [int(x) for x in grade_list]
    students_list.append(Student(fi, gr_num, grade_list))
students_dict = {student.average_sc: student for student in students_list}

for i in sorted(students_dict):
    a = students_dict[i]
    a.info()
