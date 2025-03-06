import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():

    max_number = 100
    min_number = 1
    number = random.randint(min_number, max_number)
    question = number
    correct_answer = ("yes" if is_even(number) else "no")
    
    return question, correct_answer
