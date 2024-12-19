from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(upload_to='static/users_profile_images', default='static/users_profile_images/defaultIconProfile.png' ,null=True, blank=True)
    back_image = models.ImageField(upload_to='static/users_background_images', default='static/users_background_images/defaultIconBack.png', null=True, blank=True)