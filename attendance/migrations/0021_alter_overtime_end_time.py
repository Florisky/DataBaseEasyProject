# Generated by Django 3.2.8 on 2023-05-30 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0020_alter_overtime_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 21, 29, 57, 109289)),
        ),
    ]
