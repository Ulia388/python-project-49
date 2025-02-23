import random
from brain_games.scripts.sample import welcome
from brain_games.scripts.sample import prime_number



def main():

    if __name__ == "__main__":
        main()

    name = welcome()

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):

        number = random.randint(2, 100)
        correct_answer = number
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if prime_number(number) else "no"

        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
