#!/usr/bin/env python3

from brain_games.basic import conditions_game
from brain_games.games.brain_calc import DESCRIPTION, get_question_and_answer


def main():
    conditions_game(DESCRIPTION, get_question_and_answer)


if __name__ == "__main__":
    main()