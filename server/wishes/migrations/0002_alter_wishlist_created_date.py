# Generated by Django 4.2 on 2023-04-30 22:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 30, 22, 23, 28, 431230, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]