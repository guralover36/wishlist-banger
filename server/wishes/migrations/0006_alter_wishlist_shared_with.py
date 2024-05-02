# Generated by Django 4.2 on 2023-05-30 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_profile_description'),
        ('wishes', '0005_remove_wish_image_alter_wish_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='shared_with',
            field=models.ManyToManyField(blank=True, to='users.profile'),
        ),
    ]