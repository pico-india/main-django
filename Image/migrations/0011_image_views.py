# Generated by Django 3.2.6 on 2021-11-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0010_remove_image_images_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]