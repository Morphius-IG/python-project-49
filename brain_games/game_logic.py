import sys

import prompt

from brain_games.cli import welcome_user
from brain_games.games.calc import calc
from brain_games.games.even import is_even
from brain_games.games.gcd import find_gcd
from brain_games.games.prime import is_prime
from brain_games.games.progression import get_progression


def main():
    script_name = sys.argv[0]  # Получаем имя запущенного скрипта
    if 'brain-even' in script_name:
        question = 'Answer "yes" if the number is even, ' \
            'otherwise answer "no".'
        work_function = is_even
    elif 'brain-calc' in script_name:
        question = 'What is the result of the expression?'
        work_function = calc
    elif 'brain-gcd' in script_name:
        question = 'Find the greatest common divisor of given numbers.'
        work_function = find_gcd
    elif 'brain-progression' in script_name:
        question = 'What number is missing in the progression?'
        work_function = get_progression
    elif 'brain-prime' in script_name:
        question = 'Answer "yes" if given number is prime. "\
            Otherwise answer "no".'
        work_function = is_prime
    
    name = welcome_user()
    print(question)
    counter = 0
    while counter < 3:
        expression, correct_answer = work_function()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(." 
                  f"Correct answer was '{correct_answer}'.\n"
f"Let's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')