from django.db import models
from django.utils import timezone
import pytz

# Create your models here.
class new_friend(models.Model):
	name = models.CharField(max_length=27)
	heroku_link = models.CharField(max_length=100)
	created_date = models.DateTimeField(default=(timezone.now() + timezone.timedelta(hours=7)))

