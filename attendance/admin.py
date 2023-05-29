from django.contrib import admin
from .models import Employee, Attendance, BusinessTrip, Leave, Overtime



class OvertimeAdmin(admin.ModelAdmin):
    readonly_fields = ('hours',)

class BusinessTripAdmin(admin.ModelAdmin):
    readonly_fields = ('days',)

class LeaveAdmin(admin.ModelAdmin):
    readonly_fields = ('days',)


# Register your models here.
admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(BusinessTrip, BusinessTripAdmin)
admin.site.register(Leave, LeaveAdmin)
admin.site.register(Overtime, OvertimeAdmin)

