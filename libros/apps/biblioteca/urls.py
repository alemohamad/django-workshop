from django.urls import path

from . import views

app_name = 'biblioteca_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='list-authors'),
    path('books/<pk>', views.BooksAuthorView.as_view(), name='list-books-author'),
]
