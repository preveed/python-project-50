.PHONY: lint

lint:
	poetry run flake8 .
	poetry run isort .