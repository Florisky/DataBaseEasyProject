# Generated by Django 3.2.8 on 2023-05-31 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0032_auto_20230531_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 31, 11, 13, 42, 676764)),
        ),
    ]