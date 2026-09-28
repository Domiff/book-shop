set dotenv-load

run:
    cd backend && uv run python manage.py runserver

migrate:
    cd backend && uv run python manage.py migrate

test-all:
    cd backend && uv run python manage.py test

test dir:
    cd backend && uv run python manage.py test {{dir}}

lint:
    uv run ruff check .

format:
    uv run ruff format .
