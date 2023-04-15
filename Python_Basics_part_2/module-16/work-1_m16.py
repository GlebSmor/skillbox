main = [1, 5, 3]
first = [1, 5, 5, 5]
second = [1, 3, 5, 5, 3, 3]
main.extend(first)
print('Кол-во цифр 5 при первом объединении:', main.count(5))
for _ in range(main.count(5)):
    main.remove(5)
main.extend(second)
print('Кол-во цифр 3 при втором объединении:', main.count(3))
print('Итоговый список:', main)
