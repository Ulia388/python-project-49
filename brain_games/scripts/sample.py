import random

import numpy as np
import prompt


def welcome():

    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def random_expression():

    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operations = ["+", "-", "*"]
    operation = random.choice(operations)
    expression = f"{num1} {operation} {num2}"
    return expression


def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2


def generate_progression():

    start = np.random.randint(0, 10)
    step = np.random.randint(1, 5)
    progression = [start + i * step for i in range(10)]
    num_index = np.random.randint(0, 10)
    number = progression[num_index]
    progression[num_index] = ".."

    return progression, number


def prime_number(num):

    if num % 2 == 0 or num % 3 == 0:                 # вычеркиваем все числа, делящиеся на 2 и 3
        return False
    i = 5                                             # пропускаем 4 т.к. делится на 2
    while i * i <= num:              
        if num % i == 0 or num % (i + 2) == 0:        # учитываем все числа, кот. делятся на 5, (i + 2) - учитываем число 7 
            return False
        i += 6                                        # учитываем числа 11, 17 и т.д.
    return True




