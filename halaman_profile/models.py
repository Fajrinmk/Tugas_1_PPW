from django.db import models

# Create your models here.

class Expertise (models.Model):
     #dataprofile = models.ForeignKey(DataProfil)
     expertise = models.CharField(max_length=100)

     def __str__(self):
         return self.expertise

class DataProfil(models.Model):
     username = models.CharField(max_length = 27)
     birthday = models.CharField(max_length = 6, default = '15 jul')
     gender = models.CharField(max_length = 10)
     expertise = models.ManyToManyField(Expertise)
     description = models.CharField(max_length = 100)
     email = models.EmailField()

