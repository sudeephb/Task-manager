# Generated by Django 2.0.5 on 2018-05-19 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]