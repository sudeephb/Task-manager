from django.shortcuts import render
from .models import Task

# Create your views here.


def tasks(request):
	context = {
		"tasks": Task.objects.all(),
	}

	return render(request, "tasks.html", context)