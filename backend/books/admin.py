from django.contrib import admin

from .models import Author, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = "title", "description", "published"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = "full_name", "date_birth"
