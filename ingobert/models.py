from django.db import models

# Create your models here.

class Sample(models.Model):
    project = models.CharField(max_length=40)
    source = models.CharField(max_length=40)
    label = models.CharField(max_length=40)
    text = models.TextField()

