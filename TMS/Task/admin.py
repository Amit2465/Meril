from django.contrib import admin
from .models import Profile
from .models import Task

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role') 
    search_fields = ('user__username',)  
    list_filter = ('role',) 

admin.site.register(Profile, ProfileAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assign_by', 'assigned_to', 'due_date', 'status')  
    list_filter = ('assign_by', 'assigned_to', 'status')  
    search_fields = ('title', 'description')  
    ordering = ('due_date',)  
admin.site.register(Task, TaskAdmin)
