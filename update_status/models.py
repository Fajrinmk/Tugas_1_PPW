from django.db import models
from django.utils import timezone
import pytz


class Status(models.Model):
	status = models.TextField()
	created_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=7))

class Comment(medels.Model):
	
