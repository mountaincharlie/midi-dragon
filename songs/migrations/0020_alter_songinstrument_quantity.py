# Generated by Django 3.2 on 2022-08-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0019_songinstrument_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songinstrument',
            name='quantity',
            field=models.PositiveIntegerField(blank=True, default=1, null=True),
        ),
    ]