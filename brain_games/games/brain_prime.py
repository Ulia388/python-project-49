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
    max_number = 100
    min_number = 2
    number = random.randint(min_number, max_number)
    question = f"{number}"
    correct_answer = ("yes" if prime_number(number) else "no")
    
    return question, correct_answer