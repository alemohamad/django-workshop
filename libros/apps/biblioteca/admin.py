from django.contrib import admin

# Register your models here.
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'nationality',
        'id'
    )
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'year',
        'author',
        'id'
    )
    search_fields = ('title',)
    list_filter = ('author',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
