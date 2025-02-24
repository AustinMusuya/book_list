from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView
from .serializers import BookSerializer
from rest_framework import generics

# Create your views here.

class HomeView(TemplateView):
    template_name = 'book_list_manager/home.html'

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class RetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
