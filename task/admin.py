from django.contrib import admin
from .models import  WorkersDepartment

# Register your models here.


class WorkersDeptAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'worker',
        'department'
    )
admin.site.register(WorkersDepartment, WorkersDeptAdmin)
