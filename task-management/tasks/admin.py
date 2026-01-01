from django.contrib import admin
from tasks.models import Task, TaskDetail, Project

admin.site.register(Task)
admin.site.register(TaskDetail)
admin.site.register(Project)