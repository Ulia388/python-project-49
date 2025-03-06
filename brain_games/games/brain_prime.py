import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_number(num):

    if num % 2 == 0 or num % 3 == 0:                 
        return False
    i = 5                                             
    while i * i <= num:              
        if num % i == 0 or num % (i + 2) == 0:        
            return False
        i += 6                                       
    return True
    

def get_question_and_answer():

    number = random.randint(2, 100)
    question = f"{number}"
    correct_answer = (
        "yes".strip().lower() if prime_number(number) else \
        "no".strip().lower()
    )
    
    return question, correct_answer