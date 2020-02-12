from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Nombre', max_length=100)
    nationality = models.CharField('Nacionalidad', max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('Titulo', blank=False, max_length=150)
    year = models.IntegerField('Año')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - ' + self.author.name
