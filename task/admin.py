from django.contrib import admin
from .models import  Task, WorkerTask




class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        'progress',
        'createdAt',
        'due_date'
    )
admin.site.register(Task, TaskAdmin)


admin.site.register(WorkerTask)
