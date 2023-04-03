import os
from dotenv import load_dotenv
import requests

from django.views.decorators.cache import cache_page
# -------- перенос строки --------
from textwrap import wrap

# --- _render_: функция предоставление.
# --- _redirect_: функция переключения.
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

# -------- Выбор статус задачи --------
from ToDoApp.forms import SelectStatus

# -------- Модель _ToDoList_ --------
from ToDoApp.models import ToDoList

# Поиск "_.env_" файл и переменные среды
# True: загрузить переменные среды.
# False: load_dotenv будет выполняться поиск переменной по заданному имени в среде хоста.
load_dotenv()


def index(request):
    """
    Описание:
    ---------
    Представления главного страницы _index.html_.
       * Вывод прогноз погоды: _"city_weather_update = {
                                    город: Ташкент/Нукус/Бухара....
                                    краткое описание погоды: ожидается снег/дождь,
                                    иконка,
                                    температура по цельси: 12°C/23°C/...,
                                    код страны: UZ/KK/KZ.....
                                    ветерь:  16/18/20.... км/ч
                                    влажность: 23.5% /12.4% /....
                                }"_.
       * Извлечение и вывод список задачи из БД: _"queryset = ToDoList.objects.all()"_
       * Форма выбора статус задачи: _"form = SelectStatus"_

    Аргументы:
    ----------
        request (_django.core.handlers.wsgi.WSGIRequest_): определение _POST/GET_ методов.

    Returns:
    --------
        render (_function_): функция предоставления, предоставляет все обработанные данные в шаблон _index.html_.
    """

    city_weather_update = {}
    queryset = ToDoList.objects.all()
    form = SelectStatus

    if request.method == "POST":
        try:
            lang = "ru"
            API_KEY = os.getenv("API_KEY")
            city_name = request.POST["city"]
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang={lang}"
            response = requests.get(url).json()

            city_weather_update = {
                "city": city_name.title(),
                "description": response["weather"][0]["description"],
                "icon": response["weather"][0]["icon"],
                "temperature": str(response["main"]["temp"]) + " °C",
                "country_code": response["sys"]["country"],
                "wind": str(response["wind"]["speed"]) + "km/h",
                "humidity": str(response["main"]["humidity"]) + "%",
            }
        except:
            pass

    else:
        city_weather_update = {}
        form = SelectStatus()

    context = {
        "city_weather_update": city_weather_update,
        "queryset": queryset,
        "form": form,
    }
    return render(request, "ToDoApp/index.html", context)


@require_http_methods(["POST"])  # Представление принимает только "POST" метод запроса.
@csrf_exempt  # Отключение "_csrf_" защиту для представление "_add_", для переключение к шаблону "_index.html_".
def add(request):
    """
    Описание:
    ---------
        * Функция извлекает данные _"title\task_day"_ из шаблона _index.html_
            затем записывает в БД.

    Аргументы:
    ----------
        request (_django.core.handlers.wsgi.WSGIRequest_): определение _POST/GET_ методов.

    Returns:
    --------
        redirect (_function_): переключение к главному шаблону _index.html_
    """

    # [1] _'request.POST["title"]'_: Получение значений _"title"_(Заголовок задачи) из шаблона _"index.html"_.
    # [2] _'request.POST.get("task_day")'_: Получение значений _"task_day"_(Задача дня) из шаблона _"index.html"_.
    # [3] "_str()_": Преобразование в строку.
    # [4] "_wrap()_": разбиение строку после каждого 20го символа.
    # [5] "_'\n'.join()_": соединение все элементы в строку, используя табуляцию('\n') в качестве разделителя.
    title = "\n".join(wrap(str(request.POST["title"]), width=20))
    task_day = "\n".join(wrap(str(request.POST.get("task_day")), width=20))

    # Полученные данные упоковать в модель.
    todo = ToDoList(title=title, task_day=task_day)
    # Сохранение данные в БД.
    todo.save()
    # Переключение к главному шаблону "_index.html_"
    return redirect("index")


def delete(request, todo_id):
    """
    Описание:
    ---------
        * Функция удаляет задачи по id.

    Аргументы:
    ----------
        request (_django.core.handlers.wsgi.WSGIRequest_): определение _POST/GET_ методов.
        todo_id (_int_): id задачи, получается из шаблона "_index.html_".

    Returns:
    --------
        redirect (_function_): переключение к главному шаблону _index.html_
    """

    todo = ToDoList.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")


@require_http_methods(["POST"])  # Представление принимает только "POST" метод запроса.
@csrf_exempt  # Отключение "_csrf_" защиту для представление "_update_", для переключение к шаблону "_index.html_".
def update(request, todo_id):
    """
    Описание:
    ---------
        * Функция обновляет статуз задачи по id.

    Аргументы:
    ----------
        request (_django.core.handlers.wsgi.WSGIRequest_): определение _POST/GET_ методов.
        todo_id (_int_): id задачи, получается из шаблона "_index.html_".

    Returns:
    --------
        redirect (_function_): переключение к главному шаблону _index.html_
    """

    # Получение одного конкретного id.
    todo = ToDoList.objects.get(id=todo_id)
    # Форма выбора статуса "_type:'select'_"
    form = SelectStatus(request.POST)
    if form.is_valid():
        todo.status = form.cleaned_data["status"]
    todo.save()
    return redirect("index")
