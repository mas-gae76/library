from django.contrib import admin
from .models import Author, Genre, Books


@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    list_display_links = ('title', )
    search_fields = ['title', 'author']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('initials', )
    list_display_links = ('initials', )
    search_fields = ('initials', )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    search_fields = ('name', )

