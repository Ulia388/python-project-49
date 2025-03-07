import math
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."


def get_question_and_answer():
    max_number = 100
    min_number = 1
    num1 = random.randint(min_number, max_number)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer