# Generated by Django 3.1.7 on 2021-03-16 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0047_auto_20210311_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinatoffice',
            name='reminder_time1',
            field=models.IntegerField(blank=True, default=7, null=True),
        ),
        migrations.AddField(
            model_name='coordinatoffice',
            name='reminder_time2',
            field=models.IntegerField(blank=True, default=7, null=True),
        ),
        
    ]
