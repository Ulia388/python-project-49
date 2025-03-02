import random
from brain_games.scripts.main import welcome
from brain_games.games.basic import conditions_game, random_expression


def main():

    if __name__ == "__main__":
        main()

    name = welcome()
    print("What is the result of the expression?")

    numbers = random_expression()
    correct_answer = eval(numbers)

    conditions_game(numbers, correct_answer)