from brain_games.basic import conditions_game
from brain_games.games.brain_progression import DESCRIPTION
from brain_games.games.brain_progression import get_question_and_answer


def main():
    conditions_game(DESCRIPTION, get_question_and_answer)


if __name__ == "__main__":
    main()