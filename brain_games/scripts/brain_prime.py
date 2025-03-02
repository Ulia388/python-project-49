from brain_games.games.brain_prime import DESCRIPTION, get_question_and_answer
from brain_games.basic import conditions_game, welcome

def main():
    conditions_game(DESCRIPTION, get_question_and_answer)


if __name__ == "__main__":
    main()