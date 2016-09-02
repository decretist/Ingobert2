from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sample(models.Model):
    project = models.IntegerField()
    source = models.CharField(max_length=40)
    label = models.CharField(max_length=40)
    text = models.TextField()

