from django.urls import path
from .views.department import DepartmentView, DepartmentDetailsView, DepartmentsView

urlpatterns = [
    path('department/create', DepartmentView.as_view(), name='create_department'),
    path('department/', DepartmentsView.as_view(), name='view_departments'),
    path('department/<int:id>', DepartmentDetailsView.as_view(), name='department_details')
]