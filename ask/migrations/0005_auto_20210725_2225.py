# Generated by Django 3.1.7 on 2021-07-25 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0004_auto_20210524_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='age',
            field=models.CharField(max_length=100),
        ),
    ]
