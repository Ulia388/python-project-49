import numpy as np

DESCRIPTION = "What number is missing in the progression?"
LENGTH_OF_PROGRESSION = 10


def generate_progression(start, step):
    
    progression = [start + i * step for i in range(LENGTH_OF_PROGRESSION)]
    return progression


def get_question_and_answer():
    first_number_of_progression = np.random.randint(0, 10)
    step_of_progression = np.random.randint(1, 5)
    hidden_element_index = np.random.randint(0, LENGTH_OF_PROGRESSION)

    progression = generate_progression(
        first_number_of_progression, 
        step_of_progression
    )
    
    number = progression[hidden_element_index]
    progression[hidden_element_index] = ".."
    
    question = " ".join(map(str, progression))
    correct_answer = str(number)
    
    return question, correct_answer