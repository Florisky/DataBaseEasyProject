# Generated by Django 3.2.8 on 2023-05-30 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_alter_overtime_end_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 21, 24, 19, 931921)),
        ),
    ]