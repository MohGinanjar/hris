# Generated by Django 3.1.5 on 2021-02-01 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210118_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeview',
            name='duration_work',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='worktime',
            name='duration_work',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
