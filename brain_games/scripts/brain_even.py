import random

import prompt


def welcome():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def is_even(number):
    return number % 2 == 0


def main():

    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

        print("Correct!")
        correct_answers += 1

    print(f"Congratulations, {name}!")

    if __name__ == "__main__":
        main()
