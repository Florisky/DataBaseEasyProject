from django.db import models
from django.core.exceptions import ValidationError
from datetime import date,datetime,timedelta



class AgeLimitException(Exception):
    def __init__(self, message="年龄不得小于18岁。"):
        self.message = message
        super().__init__(self.message)

class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', '男'),
        ('F', '女'),
    ]
    employee_id = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=50)
    employee_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    employee_age = models.PositiveIntegerField(default=18)
    employee_title = models.CharField(max_length=150, blank=True, null=True)
    def clean(self, *args, **kwargs):
        if self.employee_age < 18:
            raise ValidationError("年龄不得小于18岁。")
    def save(self, *args, **kwargs):
        self.clean()
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
    days = models.PositiveIntegerField(blank=True, null=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("结束日期不能早于开始日期。")

    def save(self, *args, **kwargs):
        self.clean()
        self.days = (self.end_date - self.start_date).days
        super().save(*args, **kwargs)

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    days = models.DurationField(blank=True, null=True)

    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError("结束日期不能早于开始日期。")

    def save(self, *args, **kwargs):
        self.clean()
        self.days = self.end_date - self.start_date
        super().save(*args, **kwargs)


class Overtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now() + timedelta(hours=1))
    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.hours = (self.end_time - self.start_time).total_seconds() / 3600
        super().save(*args, **kwargs)


    class Meta:
        verbose_name_plural = "OverTime"

