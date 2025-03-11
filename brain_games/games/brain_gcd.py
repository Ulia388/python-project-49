import math
import random

DESCRIPTION = "Find the greatest common divisor of given numbers."
MAX_NUMBER = 100
MIN_NUMBER = 1


def get_question_and_answer():
    
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{num1} {num2}'
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer