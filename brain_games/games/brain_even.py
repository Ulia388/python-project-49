import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER = 100
MIN_NUMBER = 1


def is_even(number):
    return number % 2 == 0


def get_question_and_answer():

    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = number
    correct_answer = ("yes" if is_even(number) else "no")
    
    return question, correct_answer
