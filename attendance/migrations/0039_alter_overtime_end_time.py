# Generated by Django 3.2.8 on 2023-05-31 03:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0038_alter_overtime_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 12, 29, 15, 136788)),
        ),
    ]
