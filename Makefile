install:
	poetry install
run:
	poetry run page_loader
lint:
	poetry run flake8 page_loader
build:
	poetry build
