import prompt
import random 


def welcome():

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def random_expression():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    expression = f"{num1} {operation} {num2}"
    return expression


def calculate(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2