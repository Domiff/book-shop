# Book Shop App

Online book store built with Django. Browse and search the catalog in the browser, manage books as a staff user, and access the same data through a REST API.

## Features

- Search books by title or description
- View full catalog and individual book pages with cover images
- Create, update, and delete books (staff only)
- User registration, login, and logout
- REST API for book CRUD operations
- Django admin panel for `Book` and `Author` models

## Stack

| Tool | Purpose |
|------|---------|
| Django 5.2 | Web framework |
| Django REST Framework | REST API |
| Pillow | Image uploads |
| python-dotenv | Environment configuration |
| SQLite / PostgreSQL | Database |
| uv | Dependency management |

## Apps

```
backend/
  core/       — project settings and routing
  books/      — catalog models, templates, and web views
  api/        — DRF viewset and serializers
  auth_user/  — registration and session auth
  manage.py
  factories.py — test data factories
nginx/        — nginx config
grafana/      — grafana, loki, promtail configs
static/       — project static files
```

## Models

**Book** — title, description, published date, price, cover image, authors (M2M)

**Author** — full name, date of birth

## Quick Start

**Requirements:** Python 3.11+, [uv](https://docs.astral.sh/uv/)

```bash
git clone git@github.com:Domiff/book-shop-app.git
cd book-shop-app

uv sync
cp .env.example .env   # set SECRET_KEY at minimum
cd backend
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Open [http://127.0.0.1:8000/shop/](http://127.0.0.1:8000/shop/)

## Routes

| URL | Access | Description |
|-----|--------|-------------|
| `/shop/` | Public | Home page with search |
| `/shop/books` | Public | Book list |
| `/shop/books/book_<id>` | Public | Book details |
| `/shop/books/create` | Staff | Add a book |
| `/shop/books/book_<id>/update` | Staff | Edit a book |
| `/shop/books/book_<id>/delete` | Staff | Delete a book |
| `/auth/register/` | Public | Sign up |
| `/auth/login/` | Public | Sign in |
| `/auth/logout/` | Auth | Sign out |
| `/api/book/` | Public | Books API |
| `/admin/` | Admin | Django admin |

## API

```
GET    /api/book/         list books
POST   /api/book/         create book
GET    /api/book/<id>/    retrieve book
PUT    /api/book/<id>/    update book
DELETE /api/book/<id>/    delete book
```

Response fields: `title`, `description`, `published`, `price`, `author`.

## Configuration

Copy `.env.example` to `.env`.

When `DEBUG=True`, the app uses SQLite. When `DEBUG=False`, it connects to PostgreSQL via the variables below.

| Variable | Required | Default |
|----------|----------|---------|
| `SECRET_KEY` | yes | — |
| `DEBUG` | no | `False` |
| `ALLOWED_HOSTS` | no | `localhost,127.0.0.1` |
| `POSTGRES_NAME`, `POSTGRES_USER`, `POSTGRES_PASSWORD` | when `DEBUG=False` | — |
| `POSTGRES_HOST` | no | `localhost` |
| `POSTGRES_PORT` | no | `5432` |


## Development

[just](https://github.com/casey/just): `just run`, `just migrate`, `just lint`, `just format`.

```bash
uv sync --dev
uv run pre-commit install
```
