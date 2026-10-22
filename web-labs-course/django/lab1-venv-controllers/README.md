# Лабораторная работа №1 (Django)

**Тема:** Создание виртуального окружения. Контроллеры и маршруты  

**Студент:** [ФИО]  
**Группа:** [Группа]  

---

## Цель работы
Настроить виртуальное пространство. Разработать контроллер приложения и организовать маршруты.

---

## Выполнение

### 1. Виртуальное окружение

```bash
mkdir MyProject
cd MyProject
python -m venv venv

# Windows:
venv\Scripts\activate

# Linux / macOS:
source venv/bin/activate

pip list
pip install -r requirements.txt   # или: pip install Django
pip list   # Django должен появиться в списке
```

### 2. Создание проекта и приложения

```bash
django-admin startproject MySite
cd MySite
python manage.py startapp news
```

### 3. Регистрация приложения

В `MySite/settings.py` в `INSTALLED_APPS` добавлено:

```python
'news.apps.NewsConfig',
```

### 4. Контроллеры (`news/views.py`)

- **index** — главная страница `/news/`
- **test** — тестовая страница `/news/test/`

Обе функции принимают `request` и возвращают `HttpResponse`.

### 5. Маршруты

**Корневой** `MySite/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
```

**Приложение** `news/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
]
```

`include` подключает маршруты приложения: префикс `news/` + пути из `news.urls`.

---

## Запуск из архива

```bash
unzip django-lab1-controllers-routes.zip
cd django-lab1-controllers
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd MySite
python manage.py migrate
python manage.py runserver
```

| URL | Страница |
|-----|----------|
| http://127.0.0.1:8000/news/ | index |
| http://127.0.0.1:8000/news/test/ | test |
| http://127.0.0.1:8000/admin/ | админка |

---

## Структура

```
django-lab1-controllers/
├── README.md
├── requirements.txt
├── screenshots/
└── MySite/
    ├── manage.py
    ├── MySite/
    │   ├── settings.py   # INSTALLED_APPS → news
    │   ├── urls.py       # include('news.urls')
    │   ├── wsgi.py
    │   └── asgi.py
    └── news/
        ├── views.py      # index, test
        ├── urls.py
        ├── apps.py
        ├── models.py
        └── migrations/
```

---

## Кратко по теории

- **venv** — изолированное окружение Python со своими пакетами.
- **Проект** (`MySite`) — настройки, корневые URL, WSGI.
- **Приложение** (`news`) — логика одной части сайта (views, models, urls).
- **Контроллер (view)** — функция, принимающая `request` и возвращающая ответ.
- **Маршрут** — связь URL с view. Корневой `urls.py` подключает urls приложений через `include`.

---

## Вывод

Создано и активировано виртуальное окружение, установлен Django, создан проект `MySite` и приложение `news`, зарегистрировано в `INSTALLED_APPS`, написаны контроллеры `index` и `test`, настроены маршруты через `include`. Освоены основы структуры Django-проекта и URL-маршрутизации.

---

## Источники

1. Django Tutorial — https://docs.djangoproject.com/en/4.2/intro/tutorial01/  
2. Virtual environments — https://docs.python.org/3/library/venv.html  
3. URL dispatcher — https://docs.djangoproject.com/en/4.2/topics/http/urls/
