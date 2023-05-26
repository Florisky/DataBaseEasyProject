import random
from django.utils import timezone
from attendance.models import Employee, Attendance, BusinessTrip, Leave, Overtime

def generate_test_data():
    # 生成职工数据
    employees = []
    for i in range(10):
        employee = Employee.objects.create(
            employee_id=f'EMP00{i}',
            employee_name=f'Employee {i}',
            employee_gender=random.choice(['Male', 'Female'])
        )
        employees.append(employee)

    # 生成出勤记录数据
    for employee in employees:
        for _ in range(2):
            check_in_time = timezone.now()
            check_out_time = check_in_time + timezone.timedelta(hours=random.randint(8, 10))
            Attendance.objects.create(
                employee=employee,
                check_in_time=check_in_time,
                check_out_time=check_out_time
            )

    # 生成出差记录数据
    for employee in employees:
        for _ in range(2):
            start_date = timezone.now().date()
            end_date = start_date + timezone.timedelta(days=random.randint(1, 5))
            BusinessTrip.objects.create(
                employee=employee,
                start_date=start_date,
                end_date=end_date
            )

    # 生成请假记录数据
    for employee in employees:
        for _ in range(2):
            start_date = timezone.now().date()
            end_date = start_date + timezone.timedelta(days=random.randint(1, 5))
            Leave.objects.create(
                employee=employee,
                start_date=start_date,
                end_date=end_date
            )

    # 生成加班记录数据
    for employee in employees:
        for _ in range(2):
            start_time = timezone.now()
            end_time = start_time + timezone.timedelta(hours=random.randint(1, 3))
            Overtime.objects.create(
                employee=employee,
                start_time=start_time,
                end_time=end_time
            )

if __name__ == '__main__':
    generate_test_data()

