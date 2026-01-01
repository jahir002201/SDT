from django.urls import path
from  tasks.views import manager_dashboard, user_dashboard,task_list, create_task, view_task, edit_task, delete_task

urlpatterns = [
    path('manager-dashboard/', manager_dashboard, name='manager-dashboard'),
    path('user-dashboard/', user_dashboard, name='user-dashboard'),
    path('task-list/', task_list, name='task-list'),
    path('create-task/', create_task, name='create-task'),
    path('view-task/<int:id>/', view_task, name='view-task'),
    path('edit-task/<int:id>/', edit_task, name='edit-task'),
    path('delete-task/<int:id>/', delete_task, name='delete-task'),
]