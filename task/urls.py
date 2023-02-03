from django.urls import path


from .views import (
    TaskView,
    TaskDetailsView,
    AssignTaskView,
    AssignTaskDetailsView
)

urlpatterns = [
    path('', TaskView.as_view()),
    path('<int:pk>/', TaskDetailsView.as_view()),
    path('assign-task/<int:id>', AssignTaskView.as_view()),
    path('assign-task-details/<int:pk>', AssignTaskDetailsView.as_view()),
]