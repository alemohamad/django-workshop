from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Author, Book

class IndexView(ListView):
    template_name = 'biblioteca/index.html'
    model = Author
    context_object_name = 'authors'

class BooksAuthorView(ListView):
    template_name = 'biblioteca/list-books-author.html'
    context_object_name = 'books'

    def get_queryset(self):
        id = self.kwargs['pk']
        list = Book.objects.filter(author=id)
        return list
