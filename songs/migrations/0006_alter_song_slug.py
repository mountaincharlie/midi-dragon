# Generated by Django 3.2 on 2022-08-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_alter_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
