from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Nombre', max_length=100)
    nationality = models.CharField('Nacionalidad', max_length=100)

    def __str__(self):
        return self.name
