from django.db import models

# Create your models here.
class Ejemplo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    number = models.IntegerField()