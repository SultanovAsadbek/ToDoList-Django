from django.contrib import admin
from ToDoApp.models import ToDoList


class AdminToDoList(admin.ModelAdmin):
    model = ToDoList
    list_display = ("id", "title", "task_day", "date_time_create", "status")


admin.site.register(ToDoList, AdminToDoList)
