from brain_games.games.brain_progression import DESCRIPTION, get_question_and_answer
from brain_games.basic import conditions_game


def main():
    conditions_game(DESCRIPTION, get_question_and_answer)


if __name__ == "__main__":
    main()