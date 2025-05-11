import random

def calc():
  operand1 = random.randint(0, 100)
  operand2 = random.randint(0, 100)
  operator = random.choice(['+', '-', '*'])
  expression = f'{operand1} {operator} {operand2}'
  result = eval(expression)
  return expression, result


#def calc():
 # name = welcome_user()
  #print('What is the result of the expression?')
#counter = 0
#while counter < 3:
 # expression, correct_answer = generate_random_expression()
  #print(f'Question: {expression}')
  #answer = prompt.string('Your answer: ')
  #if answer == str(correct_answer):
  #  print('Correct!')
   # counter += 1
  #else:
   # print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
    #Let's try again, Bill!""")
    #break
  #if counter == 3:
   # print('Congratulations, Bill!')
