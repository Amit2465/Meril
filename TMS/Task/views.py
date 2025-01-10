from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden
from .forms import RegisterForm, TaskForm
from .models import Profile, Task
from django.contrib.auth.models import User


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Creating user without saving yet
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Set the password after hashing it
            role = form.cleaned_data['role']
            # Assigning role-based permissions
            user.is_staff = role == 'admin'
            user.is_superuser = role == 'admin'
            user.is_active = True
            user.save()

            # Createing Profile instance
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.role = role
            profile.save()

            # Log the user in
            login(request, user)

            # Redirect to login page or homepage after registration
            return redirect('login')  
        else:
            # If form is not valid, include errors and display form again
            return render(request, 'register.html', {'form': form, 'error': 'Passwords do not match.'})
    else:
        form = RegisterForm()

    # Render form if GET request
    return render(request, 'register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')


@login_required(login_url='login')
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")

    tasks = Task.objects.filter(assign_by=request.user)
    employees = User.objects.filter(is_staff=False)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assign_by = request.user
            task.status = 'pending'
            task.save()
            return redirect('admin_dashboard')
    else:
        form = TaskForm()

    context = {'tasks': tasks, 'employees': employees, 'form': form}
    return render(request, 'admin_dashboard.html', context)


@login_required(login_url='login')
def employee_dashboard_view(request):
    if request.user.is_staff:
        return HttpResponseForbidden("Admins are not authorized to access the employee dashboard.")

    tasks = Task.objects.filter(assigned_to=request.user)
    return render(request, 'employee_dashboard.html', {'tasks': tasks})


@login_required(login_url='login')
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    if request.method == 'POST':
        task.status = request.POST.get('status')
        task.save()
    return redirect('employee_dashboard')


