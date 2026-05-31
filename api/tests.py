from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from factories import make_author, make_book, make_book_create_data


class ListDetailBookAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = make_book()

    def test_list(self):
        response = self.client.get(reverse("api:book-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book.title)

    def test_detail(self):
        response = self.client.get(reverse("api:book-detail", args=[self.book.pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book.title)


class CreateUpdateBookAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = make_author()
        cls.data = make_book_create_data(cls.author.pk)

    def test_create(self):
        response = self.client.post(reverse("api:book-list"), data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)

    def test_update(self):
        book = make_book()
        book.author.add(self.author)
        response = self.client.put(
            reverse("api:book-detail", args=[book.pk]), data=self.data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)


class DetailBookAPITest(APITestCase):
    def setUp(self):
        self.book = make_book()
        self.author = make_author()
        self.book.author.add(self.author)

    def test_delete(self):
        response = self.client.delete(reverse("api:book-detail", args=[self.book.pk]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
