def slicer(data, sym):
    for index, value in enumerate(data):
        if sym not in data:
            return ()

        elif value == sym and data.count(sym) == 1:
            return data[index:]

        elif value == sym and data.count(sym) > 1:
            for i, v in enumerate(data[index + 1:]):
                if v == sym:
                    return data[index:i + index + 2:]


# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 3))
# print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 0))
