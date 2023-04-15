def can_be_poly(string: str) -> bool:
    return string == string[::-1]


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))