from brain_games.scripts.sample import generate_progression, welcome


def main():

    if __name__ == "__main__":
        main()

    name = welcome()

    print("What number is missing in the progression?")

    for _ in range(3):

        progression, number = generate_progression()
        correct_answer = number
        print("Question:", " ".join(map(str, progression)))

        answer = int(input("Your answer: "))

        if answer == correct_answer:
            print("Correct!")

        else:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
