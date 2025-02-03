from rest_framework import serializers  # type: ignore
from .models import Book, Booklist,List


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookListSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Booklist
        fields = "__all__"


class ListSerializer(serializers.ModelSerializer):
     class Meta:
            model = List
            fields = "__all__"