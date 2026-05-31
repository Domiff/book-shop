set dotenv-load

run:
    uv run python manage.py runserver

migrate:
    uv run python manage.py migrate

test-all:
    uv run manage.py test

test dir:
    uv run manage.py test {{dir}}

lint:
    uv run ruff check .

format:
    uv run ruff format .
