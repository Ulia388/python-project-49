import numpy as np

DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step):
    
    progression = [start + i * step for i in range(10)]
    return progression


def get_question_and_answer():

    start = np.random.randint(0, 10)
    step = np.random.randint(1, 5)
    progression = generate_progression(start, step)
    
    num_index = np.random.randint(0, 10)
    number = progression[num_index]
    progression[num_index] = ".."
    
    question = " ".join(map(str, progression))
    correct_answer = str(number)
    
    return question, correct_answer