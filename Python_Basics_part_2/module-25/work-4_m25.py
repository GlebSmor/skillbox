class Person:
    __name = ''
    __surname = ''
    __age = 0

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Меня зовут: {self.__name} {self.__surname}\nМой возраст: {self.__age}'


class Employee(Person):
    salary = 0
    
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата: {self.salary} р'

    def salary_count(self):
        self.salary = 0


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__(self):
        return super().__str__()

    def salary_count(self):
        self.salary = 13000


class Agent(Employee):
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.sales_volume = sales_volume

    def __str__(self):
        return super().__str__()

    def salary_count(self):
        self.salary = 5000 + self.sales_volume * 5/100


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def __str__(self):
        return super().__str__()

    def salary_count(self):
        self.salary = 100 * self.hours


employee1 = Manager('Roman', 'Ivanov', 25)
employee2 = Manager('Vasily', 'Petrov', 20)
employee3 = Manager('Ivan', 'Sidorov', 19)
employee4 = Agent('Vasily', 'Ivannov', 28, 300000)
employee5 = Agent('Roman', 'Sidorov', 30, 500000)
employee6 = Agent('Ivan', 'Petrov', 42, 400000)
employee7 = Worker('Roman', 'Shastun', 18, 120)
employee8 = Worker('Petr', 'Pozov', 54, 80)
employee9 = Worker('Konstantin', 'Peskov', 32, 95)

employee_list = [employee1, employee2, employee3, employee4, employee5,
                 employee6, employee7, employee8, employee9]

for employee in employee_list:
    employee.salary_count()
    print(employee.__str__() + '\n')

