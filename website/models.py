from django.db import models

# Create your models here.

class Task(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    PRIORITY_CHOICES = [
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low'),
    ]

    
    STATUS_CHOICES = [
        ('1','To-Do'),
        ('2', 'In Progress'),
        ('3','Completed')
    ]

    
    given_id = models.PositiveSmallIntegerField(default=1)
    task_title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    priority = models.CharField(choices= PRIORITY_CHOICES , max_length=20, null=True, blank=True)
    status = models.CharField(choices= STATUS_CHOICES ,max_length=20, null=True, blank=True)
    est_time = models.CharField(max_length=50)

    due_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return (f"{self.task_title} {self.description}")