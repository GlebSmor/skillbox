from typing import List
from math import prod

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

new_floats = list(map(lambda num: round(num**3, 3), floats))
new_names = list(filter(lambda name: len(name) > 4, names))
new_numbers = prod(numbers)

print(f'{new_floats}\n{new_names}\n{new_numbers}')