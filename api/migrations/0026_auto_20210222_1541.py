# Generated by Django 3.1.5 on 2021-02-22 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20210222_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveheader',
            name='act_state1',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='act_state2',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='act_state3',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='doc_support',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='sendapp1_sts',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='sendapp2_sts',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='sendapp3_sts',
            field=models.CharField(default='NON', max_length=3),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='sendemp_sts',
            field=models.CharField(default='NON', max_length=3),
        ),
    ]
