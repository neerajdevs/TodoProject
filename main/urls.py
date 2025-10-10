from django.urls import path , include
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("" , home , name='home'),
    path("dashboard/add-tasks" , addTask , name='addTask'),
    path('home/dashboard/' ,dashboard , name='dashboard'),
    path('dashboard/edit/<int:id>/' , editTask, name='edit'),
    path('task/delete/<int:id>/' , deleteTask, name='delete'),
    path('task/toggle/<int:id>/', toggleTask, name='toggle'),
]
