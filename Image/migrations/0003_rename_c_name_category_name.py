# Generated by Django 3.2.5 on 2021-07-10 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Image', '0002_auto_20210710_1447'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_name',
            new_name='name',
        ),
    ]
