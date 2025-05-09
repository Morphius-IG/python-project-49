import secrets

import prompt

from brain_games.scripts.brain_games import main as greeting


def main():
    name = greeting()
    # print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        number = secrets.randbelow(100) + 1
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
    
        if answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!""")
            break
    if counter == 3:
        print(f"Congratulations, {name}!")