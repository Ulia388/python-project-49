.PHONY: install

install:
    uv sync     

brain-games:
    uv run brain-games

build:
    uv build

package-install:
    uv tool install dist/*.whl

make lint:
    uv run ruff check brain_games
    uv run ruff check brain_even
    uv run ruff check brain_calc
    uv run ruff check brain_gcd