import os
from collections.abc import Iterable
# test


def count_lines(path: str) -> Iterable[str]:

    for elem in os.listdir(path):
        count = 0
        if elem.endswith('.py'):
            with open(elem, 'r', encoding='utf-8') as file:
                for line in file:
                    if not line.startswith('\n') and not line.startswith('#'):
                        count += 1
            yield f'{elem}: {count}'


print(*count_lines('./'), sep='\n')
