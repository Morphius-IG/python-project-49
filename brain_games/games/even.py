import secrets


def is_even():
    expression = secrets.randbelow(101)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer