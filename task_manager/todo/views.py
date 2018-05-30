from django.shortcuts import render
from .models import Task

# Create your views here.


def tasks(request):
	context = {
		"tasks": Task.objects.all(),
	}
	if (request.method == 'POST'):
		print(request.POST)
	#print(Task.objects.get(status_text = 'todo'))
	t1 = Task.objects.first();
	print(t1.status)
	return render(request, "tasks.html", context)