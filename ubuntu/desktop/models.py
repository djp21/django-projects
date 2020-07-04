from django.db import models

class Folder(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField()
	modified_at = models.DateTimeField()
