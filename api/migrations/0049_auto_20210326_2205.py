# Generated by Django 3.1.7 on 2021-03-26 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20210316_1304'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='worktasklist',
            name='create_task',
            field=models.TimeField(blank=True, max_length=12, null=True),
        ),
        
        
    ]