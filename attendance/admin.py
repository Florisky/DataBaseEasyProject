from django.contrib import admin
from .models import Employee, AttendanceRecord, BusinessTrip, Leave, OverTime

class AttendanceRecordInline(admin.TabularInline):
    model = AttendanceRecord
    extra = 0

class BusinessTripInline(admin.TabularInline):
    model = BusinessTrip
    extra = 0

class LeaveInline(admin.TabularInline):
    model = Leave
    extra = 0

class OverTimeInline(admin.TabularInline):
    model = OverTime
    extra = 0

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'employee_gender', 'employee_age', 'employee_title', 'display_related_data')
    inlines = [AttendanceRecordInline, BusinessTripInline, LeaveInline, OverTimeInline]

    def display_related_data(self, obj):
        if obj.attendancerecord_set.exists() or obj.businesstrip_set.exists() or obj.leave_set.exists() or obj.overtime_set.exists():
            return "有相关记录"
        else:
            return "添加相关记录"

    display_related_data.short_description = "相关记录"

class OverTimeAdmin(admin.ModelAdmin):
    readonly_fields = ('hours',)

class BusinessTripAdmin(admin.ModelAdmin):
    readonly_fields = ('days',)

class LeaveAdmin(admin.ModelAdmin):
    readonly_fields = ('days',)

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(AttendanceRecord)
admin.site.register(BusinessTrip, BusinessTripAdmin)
admin.site.register(Leave, LeaveAdmin)
admin.site.register(OverTime, OverTimeAdmin)

