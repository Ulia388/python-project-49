import prompt
from brain_games.scripts.sample import welcome
from brain_games.scripts.sample import random_expression


def main():

    if __name__ == "__main__":
        main()

    name = welcome()
    print('What is the result of the expression?')

    for _ in range(3):
        expression = random_expression()
        correct_answer = eval(expression)
        print(f'Question: {expression}')

        answer = int(input('Your answer: '))

        if answer == correct_answer:
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
    print(f'Congratulations, {name}!')


    
    