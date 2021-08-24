# Generated by Django 3.1.7 on 2021-03-11 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_auto_20210311_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinatuser',
            name='lat2',
            field=models.FloatField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='coordinatuser',
            name='long2',
            field=models.FloatField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='coordinatuser',
            name='radius',
            field=models.FloatField(blank=True, default=10.0, max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='coordinatuser',
            name='radius2',
            field=models.FloatField(blank=True, default=10.0, max_length=4, null=True),
        ),
    ]
