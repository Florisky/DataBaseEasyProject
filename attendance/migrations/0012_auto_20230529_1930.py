# Generated by Django 3.2.8 on 2023-05-29 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20230529_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesstrip',
            name='days',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='days',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 29, 20, 30, 40, 61201)),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
