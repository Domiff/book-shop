from django.forms import CharField, Form, ModelForm, Textarea

from .models import Book


class CreateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "published",
            "preview",
            "price",
            "author",
        ]
        widgets = {
            "description": Textarea(attrs={"rows": 6, "cols": 80}),
        }


class UpdateBookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            "description",
            "preview",
            "price",
        ]
        widgets = {
            "description": Textarea(attrs={"rows": 6, "cols": 80}),
        }


class SearchBookForm(Form):
    query = CharField(label="Поиск", required=False)
