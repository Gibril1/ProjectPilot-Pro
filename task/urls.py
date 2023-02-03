from django.urls import path


from .views import (
    TaskView,
    TaskCreateView,
    TaskDetailsView,
    AssignTaskView,
    AssignTaskDetailsView,
    GetUserTasksView
    
)

urlpatterns = [
    path('', TaskView.as_view()),
    path('create/', TaskCreateView.as_view()),
    path('<int:pk>/', TaskDetailsView.as_view()),
    path('assign/<int:id>', AssignTaskView.as_view()),
    path('assign-details/<int:pk>', AssignTaskDetailsView.as_view()),
    path('users/', GetUserTasksView.as_view()),
]