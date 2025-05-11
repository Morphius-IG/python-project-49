import random



from brain_games.cli import welcome_user


def is_even():
    #name = welcome_user()
    #print('Answer "yes" if the number is even, otherwise answer "no".')
    #counter = 0
    #while counter < 3:
        expression = random.randint(0, 100)
        if expression % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return expression, correct_answer

        #print(f'Question: {expression}')
       # answer = prompt.string('Your answer: ')
    
        #if answer == correct_answer:
          #  print('Correct!')
         #   counter += 1
      #  else:
       #     print(f"""'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.
#Let's try again, {name}!""")
          #  break
  #  if counter == 3:
      #  print(f"Congratulations, {name}!")
#