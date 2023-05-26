from django.contrib import admin
from .models import Employee, Attendance, BusinessTrip, Leave, Overtime



# Register your models here.
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(BusinessTrip)
admin.site.register(Leave)
admin.site.register(Overtime)

