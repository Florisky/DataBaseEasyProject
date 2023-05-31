from django.db import models
from django.core.exceptions import ValidationError
from datetime import date,datetime,timedelta



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

class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    isabsenteeism = models.BooleanField(default=False)

    def clean(self, *args, **kwargs):
        overlapping_records = AttendanceRecord.objects.filter(
            employee=self.employee,
            check_out_time__gt=self.check_in_time,
            check_in_time__lt=self.check_out_time,
        ).exclude(pk=self.pk)

        if overlapping_records.exists():
            raise ValidationError("出勤时间与其他记录存在重叠。")

        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class BusinessTrip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    days = models.PositiveIntegerField(blank=True, null=True)

    def clean(self):
        super().clean()
        if self.end_date < self.start_date:
            raise ValidationError("结束日期不能早于开始日期。")

        overlaps = BusinessTrip.objects.filter(
            employee=self.employee,
            start_date__lte=self.end_date,
            end_date__gte=self.start_date,
        ).exclude(pk=self.pk)

        if overlaps.exists():
            raise ValidationError("出差时间与其他记录重叠。")

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
        super().clean()
        if self.end_date < self.start_date:
            raise ValidationError("结束日期不能早于开始日期。")

        overlapping_attendance = AttendanceRecord.objects.filter(
            employee=self.employee,
            check_out_time__gte=self.start_date,
            check_in_time__lte=self.end_date,
        )

        if overlapping_attendance.exists():
            raise ValidationError("请假时间与出勤记录重叠。")

        overlapping_business_trip = BusinessTrip.objects.filter(
            employee=self.employee,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date,
        )

        if overlapping_business_trip.exists():
            raise ValidationError("请假时间与出差记录重叠。")

    def save(self, *args, **kwargs):
        self.clean()
        self.days = self.end_date - self.start_date
        super().save(*args, **kwargs)

class OverTime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=datetime.now() + timedelta(hours=1))
    hours = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def clean(self):
        super().clean()
        if self.end_time < self.start_time:
            raise ValidationError("结束日期不能早于开始日期。")

        attendance_records = AttendanceRecord.objects.filter(employee=self.employee)
        if attendance_records.exists():
            last_check_out_time = attendance_records.latest('check_out_time').check_out_time
            if self.start_time < last_check_out_time:
                raise ValidationError("加班开始时间必须在最后一次考勤记录的结束时间之后。")

    def save(self, *args, **kwargs):
        self.clean()
        self.hours = (self.end_time - self.start_time).total_seconds() / 3600
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "OverTime"

