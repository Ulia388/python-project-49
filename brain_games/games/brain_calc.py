import random
DESCRIPTION = "What is the result of the expression?"


def get_question_and_answer():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = ["+", "-", "*"]
    operation = random.choice(operations)
    question = f"{num1} {operation} {num2}"
    correct_answer = int(eval(question))
    
    return question, correct_answer