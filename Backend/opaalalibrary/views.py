from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import viewsets  # type: ignore
from .models import Book, Booklist ,List
from .serializers import BookSerializer, BookListSerializer,ListSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookListViewSet(viewsets.ModelViewSet):
    queryset = Booklist.objects.all()
    serializer_class = BookListSerializer


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    
    
def opaalalibrary(request):
    return HttpResponse("Hello world!")
