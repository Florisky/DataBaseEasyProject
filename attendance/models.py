from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=50)
    employee_gender = models.CharField(max_length=10)

    def __str__(self):
        return self.employee_name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()

class BusinessTrip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

class Overtime(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Meta:
    verbose_name_plural = "Attendance Management System"

