# Generated by Django 3.2.8 on 2023-05-31 02:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0033_alter_overtime_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 11, 17, 27, 284026)),
        ),
    ]
