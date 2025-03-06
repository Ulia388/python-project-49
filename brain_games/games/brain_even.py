import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():

    number = random.randint(1, 100)
    question = number
    correct_answer = (
        ("yes").strip().lower() if is_even(number) 
        else ("no").strip().lower()
    )
    
    return question, correct_answer
