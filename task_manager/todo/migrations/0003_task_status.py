# Generated by Django 2.0.5 on 2018-05-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
