# Generated by Django 4.1.2 on 2022-10-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://designshack.net/wp-content/uploads/placehold.jpg', max_length=500),
        ),
    ]
