from django.urls import path

from .views import (
    DepartmentView, # create department
    DepartmentDetailsView, # edit or delete a department
    ListDepartmentsView, # get all the departments
    JoinDepartmentView, # join a department
    GetMembersOfDepartment, # list the members of a department
    GetUserDepartmentView # get all the departments a user has joined
    )

urlpatterns = [
    path('create/', DepartmentView.as_view(), name='create_department'),
    path('', ListDepartmentsView.as_view(), name='view_departments'),
    path('<int:pk>/', DepartmentDetailsView.as_view(), name='department_details'),
    path('join/<int:id>/', JoinDepartmentView.as_view(), name='join_department'),
    path('members/<int:id>/',GetMembersOfDepartment.as_view(), name='get_members_of_department' ),
    path('user/', GetUserDepartmentView.as_view(), name='get_users_departments')
]