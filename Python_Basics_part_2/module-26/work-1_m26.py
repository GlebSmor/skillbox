from collections.abc import Iterable
num = int(input('Введите число: '))


class SquaresNumbers:

    def __init__(self, number: int) -> None:
        self.number = number + 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count == self.number:
            raise StopIteration
        else:
            return self.count ** 2


def square_func(number: int) -> Iterable[int]:
    for i in range(1, number + 1):
        yield i ** 2


square_class = SquaresNumbers(num)
print('Класс-итератор')
print(*square_class)

print('\nФункция-генератор')
print(*square_func(num))

square_gen = (n ** 2 for n in range(1, num + 1))
print('\nГенераторное выражение')
print(*square_gen)
