import random
import math
from brain_games.scripts.sample import welcome

def main():

    if __name__ == "__main__":
        main()

    name = welcome()

    print('Find the greatest common divisor of given numbers.')

    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = math.gcd(num1, num2)
        print(f'Question: {num1} {num2}')
        
        answer = int(input('Your answer: '))

        if answer == correct_answer:
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return



