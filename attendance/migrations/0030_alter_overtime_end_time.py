# Generated by Django 3.2.8 on 2023-05-30 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0029_auto_20230530_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 22, 37, 33, 699649)),
        ),
    ]
