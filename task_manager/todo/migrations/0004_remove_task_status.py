# Generated by Django 2.0.5 on 2018-05-20 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
