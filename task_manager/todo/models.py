from django.db import models

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length = 128)
	due = models.DateTimeField(blank = True, null = True)
	def __str__(self):
		return (f"{self.name}")
