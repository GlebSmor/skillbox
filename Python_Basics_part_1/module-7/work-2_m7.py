years_salary = 0
for months in range(1, 13):
    salary = int(input('Введите з/п за месяц: '))
    years_salary += salary
years_salary = years_salary / months
print('Cреднегодовая зарплата =', years_salary)


