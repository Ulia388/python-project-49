import numpy as np

DESCRIPTION = "What number is missing in the progression?"

def generate_progression():

    start = np.random.randint(0, 10)
    step = np.random.randint(1, 5)
    progression = [start + i * step for i in range(10)]
    num_index = np.random.randint(0, 10)
    number = progression[num_index]
    progression[num_index] = ".."

    return progression, number

def get_question_and_answer():

    progression, number = generate_progression()
    question = " ".join(map(str, progression))
    correct_answer = str(number)
    
    return question, correct_answer
