# Generated by Django 3.2 on 2022-08-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_alter_song_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]