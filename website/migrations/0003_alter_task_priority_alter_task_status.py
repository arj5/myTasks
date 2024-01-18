# Generated by Django 5.0.1 on 2024-01-16 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_task_given_id_alter_task_priority_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('To-Do', 'To-Do'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20),
        ),
    ]