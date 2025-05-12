import secrets


def calc():
    operand1 = secrets.randbelow(101)
    operand2 = secrets.randbelow(101)
    operator = secrets.choice(['+', '-', '*'])
    expression = f'{operand1} {operator} {operand2}'
    result = eval(expression)
    return expression, result