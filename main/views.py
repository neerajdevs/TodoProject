from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from accounts.views import *
from django.http import HttpResponse
from .models import Tasks
from django.shortcuts import get_object_or_404, redirect


# Create your views here.

def home(request):
    return render(request , 'home.html')

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        user_tasks = Tasks.objects.filter(user=request.user)  # sirf current user ke tasks
        completed_count = Tasks.objects.filter(user=request.user,completed=True).count()
        pending_count = Tasks.objects.filter(user=request.user,completed=False).count()

    else:
        user_tasks = Tasks.objects.none()  # guest ke liye empty queryset

    return render(request, 'dashboard.html', {'tasks': user_tasks ,'completed_count': completed_count, 'pending_count': pending_count,})


@login_required
def addTask(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        created = request.POST.get('created')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')
        completed = request.POST.get('completed') == 'on' # Because of boolean field issue 

        task_obj= Tasks.objects.create(user = request.user , task = task , description = description , created = created , due_date = due_date , priority = priority , completed = completed)


    return render(request , 'add_tasks.html' )


@login_required
def deleteTask(request, id):
    try:
        task = Tasks.objects.get(id=id, user=request.user)
        task.delete()
        return redirect('dashboard')  # redirect to the dashboard view name
    except Tasks.DoesNotExist:
        return HttpResponse("Task not found")


@login_required
def editTask(request, id):
    try:
        task = Tasks.objects.get(id=id)
    except Tasks.DoesNotExist:
        return HttpResponse("Task not found")

    if request.method == 'POST':
        task.task = request.POST.get('task')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.priority = request.POST.get('priority')
        task.completed = request.POST.get('completed') == 'on'
        task.save()
        return redirect('dashboard')  # ya task list

    return render(request, 'edit.html', {'task': task})

def toggleTask(request, id):
    task = Tasks.objects.get(id=id, user=request.user)
    task.completed = not task.completed  # toggle True <-> False
    task.save()
    return redirect('dashboard')  # apne dashboard ka naam use karo