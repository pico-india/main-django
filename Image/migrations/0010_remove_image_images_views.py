# Generated by Django 3.2.5 on 2021-08-18 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0009_image_images_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='images_views',
        ),
    ]