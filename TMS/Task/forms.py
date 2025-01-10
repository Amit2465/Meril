from django import forms
from .models import Task
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    role = forms.ChoiceField(choices=[('employee', 'Employee'), ('admin', 'Admin')])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("confirm_password")
        username = cleaned_data.get("username")
        
        # Checking if the passwords match
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        
        # Checking if the username is already taken
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        
        return cleaned_data



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'due_date']  
        # Filtering Employees who are not staff
    assigned_to = forms.ModelChoiceField(queryset=User.objects.filter(is_staff=False), required=True)  
