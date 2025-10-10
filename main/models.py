from django.db import models
from django.contrib.auth.models import User
# Create your models here.


PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
class Tasks(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='tasks')
    task = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)   
    due_date = models.DateField()
    priority = models.CharField(max_length = 255 , choices=PRIORITY_CHOICES, default='Medium')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
