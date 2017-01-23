from __future__ import unicode_literals

from django.db import models
from django.core.validators import URLValidator


class College(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return "%s" %(self.name)

research_types = [
        ('study', 'study'),
        ('project', 'project'),
        ('paper', 'paper'),
        ('patent', 'patent'),
     ]

class ResearchWork(models.Model):
    research_type = models.CharField(choices=research_types, max_length=250, null=True, blank=True)
    topic = models.TextField()
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return "%s" %(self.link)

class Department(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return "%s" %(self.name)

class Professor(models.Model):
    name = models.CharField(max_length=250)
    email = models.TextField(null=True, blank = True)
    designation = models.CharField(max_length=250, null=True, blank=True)
    department = models.ForeignKey(Department)
    college = models.OneToOneField(College)
    phone = models.TextField(null=True, blank=True)
    area_of_interest = models.TextField(null=True, blank=True)
    research_work = models.ForeignKey(ResearchWork)
    profile_link = models.URLField(null=True, blank=True)
    display_picture = models.TextField(validators=[URLValidator()],blank=True)
    short_description = models.TextField(null=True, blank=True)
    def __str__(self):
        return "%s-%s" %(self.name, self.college)
