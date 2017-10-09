from django.db import models

class Status(models.Model):
	status = models.TextField()
	created_date = models.DateTimeField(auto_now_add=True)
