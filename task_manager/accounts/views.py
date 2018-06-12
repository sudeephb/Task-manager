from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def login_user(request):
	if request.method == "POST":
		print(request.POST)
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			print(user)
			login(request, user)
			return HttpResponseRedirect(reverse('home'))
		else:
			messages.error(request, 'Invalid Credentials')

		return render(request, 'login.html', {})
			


	return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))
