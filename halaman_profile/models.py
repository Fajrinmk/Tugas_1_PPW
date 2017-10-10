from django.db import models

# Create your models here.

class DataProfil(models.Model):
    username = models.CharField(max_length = 27)
    birthday = models.CharField(max_length = 6, default = '15 juli')
    gender = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100)
    email = models.CharField()

class Expertise (models.Model):
    dataprofile = models.ForeignKey(DataProfil)
    expertise = models.CharField(max_length=100)