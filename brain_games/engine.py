import prompt

from brain_games.cli import welcome


def run_game(description, get_question_and_answer):
    name = welcome()
    print(description)

    for _ in range(3):
        question, correct_answer = get_question_and_answer()

        print(f"Question: {question}")
        answer = prompt.string("Your answer: ")

        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
    



