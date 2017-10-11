from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class new_friend(models.Model):
	def converTime():
		return timezone.now() + timezone.timedelta(hours=7)
	name = models.CharField(max_length=27)
	heroku_link = models.CharField(max_length=27)
	created_date = models.DateTimeField(default=converTime)

