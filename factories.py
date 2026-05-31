from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker
from PIL import Image

from books.models import Author, Book

faker = Faker()
User = get_user_model()


def make_image():
    file = BytesIO()
    Image.new("RGB", (100, 100)).save(file, "JPEG")
    file.seek(0)
    return SimpleUploadedFile("test.jpg", file.read(), content_type="image/jpeg")


def make_author():
    return Author.objects.create(full_name=f"{faker.first_name()} {faker.last_name()}")


def make_book(**kwargs):
    defaults = {
        "title": faker.text(50),
        "description": faker.text(200),
        "published": faker.date_time_ad(),
        "price": faker.random_number(digits=2),
        "preview": faker.image_url(),
    }
    defaults.update(kwargs)
    return Book.objects.create(**defaults)


def make_user(**kwargs):
    defaults = {
        "username": faker.user_name(),
        "password": faker.password(),
        "email": faker.email(),
    }
    defaults.update(kwargs)
    return User.objects.create_user(**defaults)


def make_admin(**kwargs):
    kwargs.setdefault("is_staff", True)
    return make_user(**kwargs)


def make_book_create_data(author_pk):
    return {
        "title": faker.text(50),
        "description": faker.text(200),
        "published": faker.date(),
        "preview": make_image(),
        "price": faker.random_number(digits=2),
        "author": [author_pk],
    }


def make_book_update_data():
    return {
        "description": faker.text(200),
        "preview": faker.image_url(),
        "price": faker.random_number(digits=2),
    }


def make_register_credentials():
    password = faker.password()
    return {
        "username": faker.user_name(),
        "email": faker.email(),
        "password1": password,
        "password2": password,
    }


def make_login_credentials():
    return {
        "username": faker.user_name(),
        "password": faker.password(),
    }
