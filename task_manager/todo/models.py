from django.db import models

STATUS_CHOICES = (
    ('com','complete'),
    ('incom','incomplete'),
    ('to','todo'),
)

# Create your models here.
#added later
class Status(models.Model):
	status_text = models.CharField(max_length = 16, choices = STATUS_CHOICES, default = 'to', blank=False, null = False)

	def __str__(self):
		return self.status_text

class Task(models.Model):
	name = models.CharField(max_length = 128)
	due = models.DateTimeField(blank = True, null = True)
	status = models.ForeignKey(Status, on_delete = models.CASCADE)

	def __str__(self):
		return (f"{self.name}")

