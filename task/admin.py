from django.contrib import admin
from .models import Department, WorkersDepartment

# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
admin.site.register(Department, DepartmentAdmin)


class WorkersDeptAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'worker',
        'department'
    )
admin.site.register(WorkersDepartment, WorkersDeptAdmin)
