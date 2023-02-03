from django.urls import path



from .views.workers import (
    JoinDepartmentView
)

from .views import (
    TaskView,
    TaskDetailsView
)

urlpatterns = [
    
    path('join/department/<int:pk>', JoinDepartmentView.as_view(), name='department_details'),
    path('task/', TaskView.as_view()),
    path('task/<int:pk>', TaskDetailsView.as_view())
]