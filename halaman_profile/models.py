from django.db import models

# Create your models here.

class DataProfil(models.Model):
    nama = models.CharField(max_length = 27)
    birth = models.CharField(max_length = 6, default = '15 juli')
    gender = models.CharField(max_length = 10)
    description = models.CharField(max_length = 100)
    email = models.CharField()

class Expertise (models.Model):
    dataprofile = models.ForeignKey(DataProfil)
    expert = models.CharField(max_length=100)