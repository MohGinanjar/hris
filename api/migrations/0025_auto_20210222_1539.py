# Generated by Django 3.1.5 on 2021-02-22 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20210222_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveheader',
            name='crt_dt',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='leaveheader',
            name='upd_dt',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
