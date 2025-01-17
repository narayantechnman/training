from django.db import models
# Create your models here.

class Service(models.Model):
    icon = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

