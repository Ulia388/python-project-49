#!/usr/bin/env python3

from brain_games.engine import run_game
from brain_games.games.brain_calc import DESCRIPTION, get_question_and_answer


def main():
    run_game(DESCRIPTION, get_question_and_answer)


if __name__ == "__main__":
    main()