# Generated by Django 4.2 on 2023-04-30 23:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_profile_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends_of', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='images/user-images'),
        ),
    ]
