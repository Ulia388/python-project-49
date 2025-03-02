import random
import numpy as np
import prompt
from brain_games.scripts.main import welcome


def random_expression():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = ["+", "-", "*"]
    operation = random.choice(operations)
    expression = f"{num1} {operation} {num2}"
    return expression


def conditions_game(numbers, correct_answer):

    name = welcome()
    
    for _ in range(3):
        
        print(f"Question: {numbers}")

        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")

        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

    if __name__ == "__main__":
        welcome()

