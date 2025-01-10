# Generated by Django 5.1.4 on 2025-01-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_remove_task_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
    ]
