# Generated by Django 3.2 on 2021-04-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_auto_20210421_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company_id',
            field=models.CharField(default='5aa5fc8b223874.28900936', max_length=25),
        ),
    ]
