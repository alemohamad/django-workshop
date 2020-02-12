from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

class IndexView(ListView):
    template_name = 'biblioteca/index.html'
    queryset = ['Cien años de soledad', 'Harry Potter', 'El principito', 'Crónica de una muerte anunciada']
    context_object_name = 'books'
