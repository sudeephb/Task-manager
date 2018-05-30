from django.contrib import admin
from .models import Task, Status

# Register your models here.
admin.site.register(Task)
admin.site.register(Status)