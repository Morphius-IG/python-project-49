import sys
import prompt
from brain_games.even import is_even
from brain_games.calc import calc
from brain_games.cli import welcome_user




def main():
  script_name = sys.argv[0]  # Получаем имя запущенного скрипта
  if 'brain-even' in script_name:
    QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
    WORK_FUNCTION = is_even
  elif 'brain-calc' in script_name:
    QUESTION = 'What is the result of the expression?'
    WORK_FUNCTION = calc
    
  name = welcome_user()
  print(QUESTION)
  counter = 0
  while counter < 3:
    expression, correct_answer = WORK_FUNCTION()
    print(f'Question: {expression}')
    answer = prompt.string('Your answer: ')
    if answer == str(correct_answer):
      print('Correct!')
      counter += 1
    else:
      print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
    Let's try again, {name}!""")
      break
  if counter == 3:
    print(f'Congratulations, {name}!')