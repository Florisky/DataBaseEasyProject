from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
    ]
    employee_id = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=50)
    employee_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    employee_age = models.PositiveIntegerField()

    def clean(self):
        if self.employee_age < 18:
            raise models.ValidationError("年龄不能小于18岁。")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.employee_name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    isabsenteeism = models.BooleanField(default=False)

class BusinessTrip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    days = models.DurationField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.days = self.end_date - self.start_date
        super().save(*args, **kwargs)

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    days = models.DurationField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.days = self.end_date - self.start_date
        super().save(*args, **kwargs)


class Overtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    hours = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        duration = self.end_date - self.start_date
        self.hours = duration.days * 24 + duration.seconds // 3600
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "OverTime"

