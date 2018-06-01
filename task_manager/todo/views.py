from django.shortcuts import render
from .models import Task, Status

# Create your views here.


def tasks(request):
	tasks = Task.objects.all()	
	
	context = {
		'tasks' : tasks,
	}

	if (request.method == 'POST'):
		remove_id = request.POST.get('remove')
		completed_task_id = request.POST.get('done');
		if completed_task_id:
		  	completed_task = Task.objects.get(id = completed_task_id)
		#  	# print(completed_task.status)
		  	completed_task.status = Status.objects.get(id = 3)		# completed has id 3 
		#  	# print(f"{completed_task.status} - {completed_task}")
		  	completed_task.save()

		new_task = request.POST.get('newTask')
		if new_task:
			# print(new_task)
			s = Status.objects.create(status_text = 'to')
			task = Task.objects.create(name = new_task, status = s)
			task.save()

		if remove_id:
			remove_task = Task.objects.get(id = remove_id)
			print(remove_task)
			remove_task.delete()



	return render(request, "tasks.html", context)