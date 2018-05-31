from django.shortcuts import render
from .models import Task, Status

# Create your views here.


def tasks(request):
	tasks = Task.objects.all()	
	# todoTasks = []
	# for task in tasks:
	# 	if task.status.status_text == 'to':
	# 		todoTasks.append(task)

	# comTasks = []
	# for task in tasks:
	# 	if task.status.status_text == 'com':
	# 		comTasks.append(task)

	# incomTasks = []
	# for task in tasks:
	# 	if task.status.status_text == 'incom':
	# 		incomTasks.append(task)


	# context = {
	# 'todoTasks': todoTasks,
	# 'comTasks': comTasks,
	# 'incomTasks': incomTasks,
	# }
	context = {
		'tasks' : tasks,
	}

	if (request.method == 'POST'):
		completed_task_id = request.POST.get('todo');
		if completed_task_id:
		 	# print(f"Completed task id : {request.POST.get('todo')}")
		 	completed_task = Task.objects.get(id = completed_task_id)
		 	print(completed_task.status)
		 	completed_task.status = Status.objects.get(id = 3)		# completed has id 3 
		 	print(f"{completed_task.status} - {completed_task}")
		 	completed_task.save()



	return render(request, "tasks.html", context)