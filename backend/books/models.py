from django.db import models


def path_for_preview(instance: "Book", file_name: str) -> str:
    path = f"previews/{instance.title}/{file_name}"
    return path


class Book(models.Model):
    title = models.CharField(
        null=False, blank=False, max_length=50, verbose_name="Название книги"
    )
    description = models.CharField(
        null=False, blank=False, max_length=200, verbose_name="Описание книги"
    )
    published = models.DateField(
        null=False, blank=False, verbose_name="Дата публикации"
    )
    author = models.ManyToManyField("Author", verbose_name="Автор книги")
    price = models.DecimalField(
        null=False,
        blank=False,
        max_digits=6,
        decimal_places=2,
        verbose_name="Стоимость книги",
    )
    preview = models.ImageField(
        upload_to=path_for_preview, verbose_name="Изображение книги"
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(
        null=False, blank=False, max_length=50, verbose_name="Полное имя автора"
    )
    date_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    def __str__(self):
        return self.full_name
