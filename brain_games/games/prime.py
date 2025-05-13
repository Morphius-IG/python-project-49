import secrets


def is_prime():
    expression = secrets.randbelow(101)
    for i in range(2, expression):
        if expression % i == 0:
            correct_answer = 'no'
            break
        else:
            correct_answer = 'yes'
    return expression, correct_answer