from django.db import models
import datetime
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):
    date = models.DateTimeField(default=datetime.datetime.today)
    image = models.ImageField(upload_to='images/')
    views = models.IntegerField(default=0)
    downloads = models.IntegerField(default=0)
    tags = models.CharField(max_length=300, null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    