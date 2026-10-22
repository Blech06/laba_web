# Лабораторная работа №1 (Django)

**Тема:** Создание виртуального окружения. Контроллеры и маршруты  

**Студент:** Мержоев Ислам Игоревич
**Группа:** ПИЖ-б-о-25-1

---

## Цель работы
Настроить виртуальное пространство. Разработать контроллер приложения и организовать маршруты.

---

## Выполнение

### 1. Создание виртуального окружения

```bash
# Создаём папку проекта
mkdir MyProject
cd MyProject

# Создаём виртуальное окружение
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux / macOS)
source venv/bin/activate

# Проверка
pip list
```

### 2. Установка Django

```bash
pip install Django
# или
pip install -r requirements.txt

pip list   # убеждаемся, что Django появился в списке
```

### 3. Создание проекта

```bash
django-admin startproject MySite
cd MySite
```

Структура после создания:

```
MySite/
├── manage.py
└── MySite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

### 4. Запуск отладочного сервера

```bash
python manage.py runserver
```

### 5. Создание приложения `news`

```bash
python manage.py startapp news
```

### 6. Регистрация приложения

В файле `MySite/settings.py` в список `INSTALLED_APPS` добавлено:

```python
'news.apps.NewsConfig',
```

### 7. Контроллеры (views.py)

Файл `news/views.py`:

- **index** — главная страница приложения (`/news/`)
- **test** — тестовая страница (`/news/test/`)

### 8. Маршруты

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

---

## Как запустить проект из архива

```bash
# 1. Распаковать архив
unzip django-lab1-venv-controllers-routes.zip
cd django-lab1

# 2. Создать и активировать виртуальное окружение
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 3. Установить зависимости
pip install -r requirements.txt

# 4. Перейти в папку проекта и запустить
cd MySite
python manage.py migrate      # создать sqlite БД
python manage.py runserver
```

После запуска:

| URL | Страница |
|-----|----------|
| http://127.0.0.1:8000/news/ | index (главная новостей) |
| http://127.0.0.1:8000/news/test/ | test |
| http://127.0.0.1:8000/admin/ | админка Django |

---

## Вывод

В ходе лабораторной работы:

1. Создано и активировано виртуальное окружение.
2. Установлен Django.
3. Создан проект `MySite` и приложение `news`.
4. Приложение зарегистрировано в `INSTALLED_APPS`.
5. Написаны контроллеры `index` и `test`.
6. Организованы маршруты: корневой `urls.py` подключает маршруты приложения через `include`.

Освоены базовые понятия Django: проект, приложение, views (контроллеры), URL-маршрутизация.

---
