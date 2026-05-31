import shutil
import tempfile

from django.test import TestCase, override_settings
from django.urls import reverse

from books.models import Book
from factories import (
    make_admin,
    make_author,
    make_book,
    make_book_create_data,
    make_book_update_data,
    make_user,
)

TEMP_MEDIA_ROOT = tempfile.mkdtemp()


class MainViewTest(TestCase):
    def test_main(self):
        response = self.client.get(reverse("books:main"))
        self.assertEqual(response.status_code, 200)


class ListDetailBookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = make_user()
        cls.author = make_author()
        cls.book = make_book()
        cls.book.author.add(cls.author)

    def test_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("books:books"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_detail(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("books:book", args=[self.book.id]))
        self.assertEqual(response.status_code, 200)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class CreateUpdateRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = make_user()
        cls.admin = make_admin()
        cls.author = make_author()
        cls.create_data = make_book_create_data(cls.author.pk)
        cls.update_data = make_book_update_data()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def test_create(self):
        self.client.force_login(self.admin)
        response = self.client.post(reverse("books:create"), data=self.create_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 1)

    def test_not_staff_create(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse("books:create"), data=self.create_data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Book.objects.count(), 0)

    def test_update(self):
        self.client.force_login(self.admin)
        book = make_book()
        book.author.add(self.author)
        response = self.client.post(
            reverse("books:update", args=[book.pk]), data=self.update_data
        )
        self.assertEqual(response.status_code, 302)

    def test_not_staff_update(self):
        self.client.force_login(self.user)
        book = make_book()
        book.author.add(self.author)
        response = self.client.post(
            reverse("books:update", args=[book.pk]), data=self.update_data
        )
        self.assertEqual(response.status_code, 403)


class DeleteRecipeTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = make_user()
        cls.admin = make_admin()
        cls.author = make_author()
        cls.book = make_book()
        cls.book.author.add(cls.author)

    def test_delete(self):
        self.client.force_login(self.admin)
        response = self.client.delete(reverse("books:delete", args=[self.book.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 0)

    def test_not_staff_delete(self):
        self.client.force_login(self.user)
        response = self.client.delete(reverse("books:delete", args=[self.book.pk]))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Book.objects.count(), 1)
