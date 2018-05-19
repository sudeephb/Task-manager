from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
	
	return render(request, "index.html")


def tasks(request):
	context = {
		"tasks": Task.objects.all(),
	}

	return render(request, "tasks.html", context)