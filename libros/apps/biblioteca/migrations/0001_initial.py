# Generated by Django 3.0.1 on 2020-02-12 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('nationality', models.CharField(max_length=100, verbose_name='Nacionalidad')),
            ],
        ),
    ]
