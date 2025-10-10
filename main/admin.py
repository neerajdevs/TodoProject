from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display=['task' , 'created' , 'due_date']
    search_fields = ['task' , 'user__username']
    list_filter = ['due_date']