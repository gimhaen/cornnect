# Generated by Django 4.2.7 on 2024-05-23 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_movie_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='talks_count',
            field=models.IntegerField(default=0),
        ),
    ]
