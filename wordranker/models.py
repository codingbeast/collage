from django.db import models

# Create your models here.
class words(models.Model):
    url = models.CharField(max_length=100)
    word = models.CharField(max_length=50)
    count = models.IntegerField()