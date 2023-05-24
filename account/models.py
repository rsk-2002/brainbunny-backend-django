from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=255)