# Generated by Django 3.1.7 on 2021-03-04 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_timeview_data_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='worktasklist',
            name='data_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,db_constraint=False, to='api.masteremployee'),
        ),
        migrations.AddField(
            model_name='worktime',
            name='data_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,db_constraint=False, to='api.masteremployee'),
        ),
       
    ]
