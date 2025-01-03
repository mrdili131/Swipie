from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_imgs/',default='profile_imgs/default_user.png')
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)