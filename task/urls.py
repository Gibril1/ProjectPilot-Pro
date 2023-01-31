from django.urls import path

from .views.department import (
    DepartmentView, 
    DepartmentDetailsView, 
    DepartmentsView
    )

from .views.workers import (
    JoinDepartmentView
)

urlpatterns = [
    path('department/create', DepartmentView.as_view(), name='create_department'),
    path('department/', DepartmentsView.as_view(), name='view_departments'),
    path('department/<int:pk>', DepartmentDetailsView.as_view(), name='department_details'),
    path('join/department/<int:pk>', JoinDepartmentView.as_view(), name='department_details')
]