import numpy as np

DESCRIPTION = "What number is missing in the progression?"
LENGTH_OF_PROGRESSION = 10
FIRST_NUMBER_OF_PROGRESSION = np.random.randint(0, 10)
STEP_OF_PROGRESSION = step = np.random.randint(1, 5)
HIDDEN_ELEMENT = np.random.randint(0, 10)


def generate_progression(start, step):
    
    progression = [start + i * step for i in range(LENGTH_OF_PROGRESSION)]
    return progression


def get_question_and_answer():

    progression = generate_progression(
        FIRST_NUMBER_OF_PROGRESSION, 
        STEP_OF_PROGRESSION
    )
    
    number = progression[HIDDEN_ELEMENT]
    progression[HIDDEN_ELEMENT] = ".."
    
    question = " ".join(map(str, progression))
    correct_answer = str(number)
    
    return question, correct_answer