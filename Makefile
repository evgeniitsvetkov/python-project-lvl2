install:
	poetry install

gendiff:
	poetry run genfiff

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

