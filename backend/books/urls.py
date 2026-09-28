from django.urls import path

from .views import (
    BookSearchView,
    CreateBookView,
    DeleteBookView,
    DetailBookView,
    ListBookView,
    UpdateBookView,
)

app_name = "books"

urlpatterns = [
    path("", BookSearchView.as_view(), name="main"),
    path("books", ListBookView.as_view(), name="books"),
    path("books/book_<int:pk>", DetailBookView.as_view(), name="book"),
    path("books/book_<int:pk>/delete", DeleteBookView.as_view(), name="delete"),
    path("books/create", CreateBookView.as_view(), name="create"),
    path("books/book_<int:pk>/update", UpdateBookView.as_view(), name="update"),
]
