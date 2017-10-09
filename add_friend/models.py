from django.db import models

# Create your models here.
class new_friend(models.Model):
	name = models.CharField(max_length=27)
	heroku_link = models.CharField(max_length=27)