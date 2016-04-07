from django.shortcuts import render,get_object_or_404
from recommender.models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



@login_required(login_url="/login/")
def index(request):
#get the recommender tasks that have been published
	tasks = Task.objects.filter(published=True)
	#now return the rendered template
	return render(request, 'recommender/index.html',{'tasks':tasks})

@login_required(login_url="/login/")
def task(request,slug):
	# get the Task object
	task = get_object_or_404(Task, slug=slug)
	# now return the rendered template
	return render(request, 'recommender/task.html',{'task':task})

@login_required(login_url="/login/")
def logout_view(request):
	logout(request)
	# Redirect to a success page
	return HttpResponseRedirect("/account/loggedout/")