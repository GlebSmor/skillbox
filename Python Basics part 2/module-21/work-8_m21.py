def unwrap(*args):
    def flatten(a_list):
        result = []
        for e in a_list:
            if isinstance(e, int):
                result.append(e)
            else:
                result.extend(flatten(e))
        return result
    return flatten(args)


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(unwrap(nice_list))