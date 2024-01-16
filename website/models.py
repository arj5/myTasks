from django.db import models

# Create your models here.

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    task_title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    priority = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    est_time = models.CharField(max_length=50)
    due_date = models.CharField(max_length=50)

    def __str__(self):
        return (f"{self.task_title} {self.description}")
