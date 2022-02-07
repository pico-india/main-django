# Generated by Django 3.2.5 on 2021-07-28 08:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_pic', models.ImageField(default='default-pic.png', upload_to='images/')),
                ('bio', models.CharField(max_length=300, null=True)),
                ('link_insta', models.CharField(max_length=2083, null=True)),
                ('link_fb', models.CharField(max_length=2083, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]