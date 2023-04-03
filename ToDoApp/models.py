from django.db import models
from django.utils.translation import gettext_lazy as _


class ToDoList(models.Model):
    """
    Описание:
    ---------
        Модель данных.
        Создание и соединение таблиц в БД sqlite3. 

    Аргументы:
    ----------
        models (_type_): _description_

    Атрибуты:
    ---------
        title (_str_): заголовок задачи дня, максимальное количество значений 50.
        task_day (_str_): задача дня, максимальное количество значений 300.
        date_time_create (_datetime_): дата и время задачи.
        status (_str_): статус задачи, максимальное количество значений 15.
        
    Returns:
    --------
        self.title(_str_): возврат статус задачи, для отображение всех данных в админке django. 
    """
    
    title = models.CharField(_("Заголовок задачи дня"), max_length=50)
    task_day = models.TextField(_("Задача дня"), max_length=300)
    date_time_create = models.DateTimeField(_("Дата и время создания"), auto_now_add=True)
    status = models.CharField(_("Статус задачи"), max_length=15)
    
    def __str__(self) -> str:
        return self.title
    