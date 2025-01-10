from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('employee_dashboard/', views.employee_dashboard_view, name='employee_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('employee/update-task-status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]