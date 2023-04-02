from django.urls import path

# -------- Главная страница --------
from ToDoApp.views import index

# -------- Добавление задачи -------
from ToDoApp.views import add

# -------- Удаление задачи ---------
from ToDoApp.views import delete

# -------- Обновление статус задачи --------
from ToDoApp.views import update


urlpatterns = [
    path("", index, name="index"),
    path("add", add, name="add"),
    path("delete/<int:todo_id>/", delete, name="delete"),
    path("update/<int:todo_id>/", update, name="update"),
]
