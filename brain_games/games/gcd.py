import secrets

def find_gcd():
  a = 1
  b = 101
  number1 = a + secrets.randbelow(b - a + 1)
  number2 = a + secrets.randbelow(b - a + 1)
  expression = f'{number1} {number2}'
  min_number = min(number1, number2)
  result = []
  for i in range(1, min_number + 1):
    if number1 % i == 0 and number2 % i == 0:
      result.append(i)
  return expression, max(result)