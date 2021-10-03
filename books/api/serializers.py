from rest_framework import serializers
from ..models import Books, Author, Genre


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['initials']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description', 'image', 'release_date', 'genre']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)
    genre = GenreSerializer(many=True)

    class Meta:
        model = Books
        fields = ['title', 'author', 'genre']
