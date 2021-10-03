from rest_framework import serializers
from ..models import Books, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description', 'image', 'release_date']
