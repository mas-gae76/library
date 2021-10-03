from django.db import models
from .functions import get_timestamp_path_book, get_timestamp_path_auth


class Genre(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Жанры'
        verbose_name = 'Жанр'
        ordering = ['name']


class Author(models.Model):
    image = models.ImageField(verbose_name='Фото автора', blank=True, upload_to=get_timestamp_path_auth)
    birthday = models.DateField(verbose_name='Дата рождения', auto_now_add=False)
    initials = models.CharField(verbose_name='ФИО', unique=True, max_length=40)

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'
        ordering = ['initials']

    def __str__(self):
        return self.initials


class Books(models.Model):
    title = models.CharField(verbose_name='Название', max_length=60, unique=True)
    author = models.ManyToManyField(Author, verbose_name='Авторы')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение книги', upload_to=get_timestamp_path_book)
    release_date = models.DateField(verbose_name='Дата выпуска',auto_now_add=False)
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
        ordering = ['title']

    def __str__(self):
        return self.title
