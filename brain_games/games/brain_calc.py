import random

DESCRIPTION = "What is the result of the expression?"
ARITHMETIC_OPERATIONS = ("+", "-", "*")
MAX_NUMBER = 100
MIN_NUMBER = 1


def get_operation(num1, num2, operation):
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    return str(correct_answer)


def get_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(ARITHMETIC_OPERATIONS)
    
    question = f"{num1} {operation} {num2}"
    answer = get_operation(num1, num2, operation)
    
    return question, answer