import secrets


def get_progression():
    first_number = secrets.randbelow(100)
    step = secrets.randbelow(4) + 1
    hidden_number_index = secrets.randbelow(10)
    set_numbers = []
    for _ in range(1, 11):
        set_numbers.append(str(first_number))
        first_number += step
    correct_answer = set_numbers[hidden_number_index]
    set_numbers[hidden_number_index] = '..'
    expression = ' '.join(set_numbers)
    return expression, correct_answer