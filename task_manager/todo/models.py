from django.db import models

STATUS_CHOICES = (
    ('com','complete'),
    ('incom','incomplete'),
    ('to','todo'),
)

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length = 128)
	due = models.DateTimeField(blank = True, null = True)
	status = models.CharField(max_length = 16, choices = STATUS_CHOICES, default = 'to', blank = False, null = False)

	def __str__(self):
		return (f"{self.name}")
