# Generated by Django 3.2.8 on 2023-05-30 13:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0028_alter_overtime_end_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='overtime',
            options={},
        ),
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 30, 22, 35, 18, 81309)),
        ),
    ]