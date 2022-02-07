from typing import DefaultDict
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pf_pic = models.ImageField(default = 'default-pic.jpg', upload_to='images/')
    bio = models.CharField(max_length=300, null=True)
    insta = models.CharField(max_length=100, null=True)
    fb = models.CharField(max_length=100, null=True)


    def __str__(self) -> str:
        return f'{self.user.username} Profile'
