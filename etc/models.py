from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UnavailableQuery(models.Model):
    query = models.TextField()
    frequency = models.IntegerField(default=1)

    def __str__(self):
        return "%s - %s" %(query, frequency)
