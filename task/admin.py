from django.contrib import admin
from .models import  Task, WorkerTask, Project




class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        'progress',
        'created_at',
        'due_date'
    )
admin.site.register(Task, TaskAdmin)

admin.site.register(Project)
admin.site.register(WorkerTask)
