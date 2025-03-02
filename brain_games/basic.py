import prompt


def welcome():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name

    
def conditions_game(description, get_question_and_answer):
    name = welcome()
    print(description)

    for _ in range(3):
        (
        question,
        correct_answer,
        ) = get_question_and_answer()

        print(f"Question: {question}")
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



