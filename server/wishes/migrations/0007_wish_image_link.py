# Generated by Django 4.2 on 2023-05-30 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishes', '0006_alter_wishlist_shared_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='wish',
            name='image_link',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
