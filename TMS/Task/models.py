from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    def __str__(self):
        return self.user.username



class Task(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField()  
    assign_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')  
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')  
    due_date = models.DateField()  
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')],
        default='Pending'
    )  

    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.title
