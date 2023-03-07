from collections import Counter

# вариант нормального человека
# def can_be_poly(string: str) -> bool:
#     return string == string[::-1]

# вариант курильщика


def can_be_poly(string: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 2


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))