# Generated by Django 3.1.5 on 2021-02-18 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20210218_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingcalendarCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arriv_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('group_id', models.CharField(choices=[('N1', 'N1'), ('N2', 'N2'), ('N3', 'N3'), ('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7'), ('S8', 'S8'), ('S9', 'S9'), ('S10', 'S10'), ('S11', 'S11'), ('P1', 'P2'), ('P2', 'P2')], max_length=4)),
                ('yyyy', models.CharField(max_length=4)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user_id', models.CharField(max_length=15)),
            ],
        ),
    ]
