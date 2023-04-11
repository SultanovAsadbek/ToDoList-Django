![Header](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/prj_name.gif)

## Описание
Оптимизируйте свои задачи с помощью ToDoList Django, которая поможет вам планировать повседневные задачи и более эффективно управлять своим временем. Благодаря простому в использовании и интуитивно понятному интерфейсу ToDoList Django гарантирует, что вы будете на правильном пути и будете видеть четкий прогресс в каждой задаче. Благодаря нашей простой, интуитивно понятной платформе и интеграции с OpenWeatherMap вы теперь можете быстро и точно планировать свои ежедневные задачи, следя за погодой. 
<br> Поднимите свою продуктивность на новый уровень с ToDoList Django!

Возможности ПО:
- Добавление задачи в БД.
- Просмотр задачи.
- Удаление задачи.
- Прогноз погоды.
- Указать статус задачи.
- Обновление статус задачи.
- Красивый админ панель.
 
## Язык программирование
![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python&logoColor=yellow)

## Технологии
![Django](https://img.shields.io/badge/Django-black?style=for-the-badge&logo=django&logoColor=green)
![Sqlite](https://img.shields.io/badge/sqlite3-black?style=for-the-badge&logo=sqlite&logoColor=blue)
![HTML](https://img.shields.io/badge/HTML5-black?style=for-the-badge&logo=HTML5&logoColor=orange)
![CSS](https://img.shields.io/badge/CSS3-black?style=for-the-badge&logo=CSS3&logoColor=blue)

![.env](https://img.shields.io/badge/.env-black?style=for-the-badge&logo=.env&logoColor=green)
![Django](https://img.shields.io/badge/django_jet_reboot-black?style=for-the-badge&logo=Vectorworks&logoColor=red)
![API](https://img.shields.io/badge/API-black?style=for-the-badge&logo=Vectorworks&logoColor=blue)
![OpenWeatherMap](https://img.shields.io/badge/openweathermap-black?style=for-the-badge&logo=Vectorworks&logoColor=blue)



## Интерфейс
![main_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/main_page.png)
> **Рис. 1**  Главная страница пользователя
---


![none_status](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/none_status.png)
![not_completed](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/not_completed.png)
![in_progress](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/in_progress.png)
![completed](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/completed.png)
> **Рис. 2** Статусы задачи
---


![main_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/main_admin_page.png)
> **Рис. 3** Главная страница администратора
---


![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/Example/Project_assets/taks_list_admin_page.png)
> **Рис. 4** Список составленных задач в странице администратора


## Установка и запуск проекта
**Шаг 1 :**

![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/main/Project_assets/step-1_installing.png)
> Выбираем  <u>Download ZIP</u>, скачивается проект в архивированном виде.
---


**Шаг 2 :**

![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/main/Project_assets/step-2_installing.png)
> Извлечём скачанный файл.
---


**Шаг 3 :**

![taks_list_admin_page](https://github.com/SultanovAsadbek/ToDoList-Django/blob/main/Project_assets/step-3_installing.png)
> Открываем проект в удбном нам редакторе, в моём случай это VS Code.
---


**Шаг 4 :**
> Создаём [виртуальное окружение](https://pyneng.readthedocs.io/ru/latest/book/01_intro/virtualenv.html) для того чтобы:
+ изолировать проекты друг от друга </li>
+ не засорять систему </li>
+ установить файл зависимости локально </li>
+ выполнения программы внутри этого окружения </li>

```
python -m venv venv
```

**Шаг 5 :**
> Активируем виртуальное окружение

``` 
./venv/scripts/activate
```

**Шаг 6:**
> Переходим в директорию проекта

```
cd ToDoList-Django-main
```

**Шаг 7:**
> Установливаем все необходимые библиотеки из файл зависимости

```
pip install -r requirements.txt
```


**Шаг 8 :**
> Создадим таблицы в базе данных затем производим миграцию 

```
python manage.py makemigrations ToDoApp
```

```
python manage.py migrate ToDoApp
```

**Шаг 9:**
> Создадим файл ```.env``` в которм будет [пременные среды](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1), в директорию ```ToDoList-Django-main\aToDoList\```.
<br> В файл ```.env``` вставляем следующие данные:

```
#
# _.env_ файле хранятся конфиденциальные данные.
#

# -------- settings.py --------
SECRET_KEY=django-insecure-jlj&%yxsr5q9_85eoyr0ek7qvi5zn8$37bzu_vg!q$%7y*wm1_
DEBUG=False

# -------- views.py --------
API_KEY=3ad14039ad77957668cd1735d7272232
``` 


**Шаг 10:**
> Запускаем локальный сервер:

```
python manage.py runserver
```
