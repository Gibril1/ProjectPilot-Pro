from django.contrib import admin
from .models import User, WorkersProfile, HODProfile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'role'
    )
admin.site.register(User, UserAdmin)


class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'
    )
admin.site.register(WorkersProfile, WorkerAdmin)


class HODAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'
    )
admin.site.register(HODProfile, HODAdmin)

