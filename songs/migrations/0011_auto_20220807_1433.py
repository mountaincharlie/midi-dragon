# Generated by Django 3.2 on 2022-08-07 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('songs', '0010_alter_song_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='project_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='songs.projecttype'),
        ),
        migrations.AlterField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='site_user', to=settings.AUTH_USER_MODEL),
        ),
    ]