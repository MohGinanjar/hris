# Generated by Django 3.1.7 on 2021-03-02 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_auto_20210302_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeview',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worktasklist',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='worktime',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]