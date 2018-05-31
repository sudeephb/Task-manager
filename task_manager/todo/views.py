from django.shortcuts import render
from .models import Task

# Create your views here.


def tasks(request):
	tasks = Task.objects.all()	
	todoTasks = []
	for task in tasks:
		if task.status == 'to':
			todoTasks.append(task)

	comTasks = []
	for task in tasks:
		if task.status == 'com':
			comTasks.append(task)

	incomTasks = []
	for task in tasks:
		if task.status == 'incom':
			incomTasks.append(task)


	context = {
	'todoTasks': todoTasks,
	'comTasks': comTasks,
	'incomTasks': incomTasks,
	}

	if (request.method == 'POST'):
		print(request.POST)

	return render(request, "tasks.html", context)