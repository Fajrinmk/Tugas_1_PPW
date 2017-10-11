from django.db import models

class Status(models.Model):
	def converTime():
		return timezone.now() + timezone.timedelta(hours=7)
	status = models.TextField()
	created_date = models.DateTimeField(default=converTime)
