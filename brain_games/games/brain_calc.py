import random

DESCRIPTION = "What is the result of the expression?"
ARITHMETIC_OPERATIONS = ("+", "-", "*")


def get_question_and_answer():
    max_number = 100
    min_number = 1
    num1 = random.randint(min_number, max_number)
    num2 = random.randint(min_number, max_number)
    operation = random.choice(ARITHMETIC_OPERATIONS)
    
    question = f"{num1} {operation} {num2}"
    
    if operation == "+":
        correct_answer = num1 + num2
    elif operation == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    
    return question, str(correct_answer)