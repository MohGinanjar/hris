# Generated by Django 3.1.7 on 2021-03-09 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20210308_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveheader',
            name='data_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,db_constraint=False ,to='api.masteremployee'),
        ),
        migrations.AlterField(
            model_name='timeview',
            name='data_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,db_constraint=False, related_name='data_timeview', to='api.masteremployee'),
        ),
        migrations.AlterField(
            model_name='worktasklist',
            name='data_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,db_constraint=False ,related_name='data_worktask', to='api.masteremployee'),
        ),
        migrations.AlterField(
            model_name='worktime',
            name='data_emp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,db_constraint=False ,related_name='data_worktime', to='api.masteremployee'),
        ),
    ]
