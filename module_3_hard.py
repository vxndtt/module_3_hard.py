data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    numbers_sum = 0
    strings_sum = 0

    def rec(data):
        nonlocal numbers_sum, strings_sum
        if isinstance(data, tuple) or isinstance(data, list) or isinstance(data, set):
            for i in data:
                rec(i)
        elif isinstance(data, dict):
            for value in data.values():
                rec(value)
            for key in data.keys():
                rec(key)
        else:
            if isinstance(data, int):
                numbers_sum += data
            else:
                strings_sum += len(data)

    rec(data_structure)
    return numbers_sum + strings_sum


result = calculate_structure_sum(data_structure)
print(result)