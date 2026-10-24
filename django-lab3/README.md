# Лабораторная работа №3: Шаблоны. Админка Django

**Студент:** Мержоев Ислам Игоревич  
**Группа:** ПИЖ-б-о-25-1  
**Технология:** Python + Django  

## Содержание

- [Цель работы](#цель-работы)
- [Теоретическое обоснование](#теоретическое-обоснование)
- [Выполнение работы](#выполнение-работы)
  - [1. Вывод данных модели в браузер (без шаблонов)](#1-вывод-данных-модели-в-браузер-без-шаблонов)
  - [2. Создание шаблонов](#2-создание-шаблонов)
  - [3. Рендеринг шаблона](#3-рендеринг-шаблона)
  - [4. Директивы, теги и фильтры](#4-директивы-теги-и-фильтры)
  - [5. Локализация и форматирование даты](#5-локализация-и-форматирование-даты)
  - [6. Сортировка новостей](#6-сортировка-новостей)
  - [7. Работа с админкой Django](#7-работа-с-админкой-django)
  - [8. Регистрация модели в админке](#8-регистрация-модели-в-админке)
  - [9. Настройка Meta и verbose_name](#9-настройка-meta-и-verbose_name)
  - [10. Настройка отображения в админке (ModelAdmin)](#10-настройка-отображения-в-админке-modeladmin)
  - [11. Валидация и миграции](#11-валидация-и-миграции)
- [Структура проекта](#структура-проекта)
- [Код ключевых файлов](#код-ключевых-файлов)
- [Проверка работоспособности](#проверка-работоспособности)
- [Контрольные вопросы](#контрольные-вопросы)
- [Вывод](#вывод)
- [Список использованных источников](#список-использованных-источников)

---

## Цель работы

Научиться выводить данные из модели в браузер с помощью шаблонов Django, освоить шаблонизатор (директивы, теги, фильтры), настроить и кастомизировать админ-панель Django.

---

## Теоретическое обоснование

**Шаблон (template)** — HTML-файл с специальным синтаксисом Django Template Language (DTL). Позволяет отделять представление от логики.

**Рендеринг** — процесс наполнения шаблона данными из контекста и формирования готовой HTML-страницы.

**Контекст** — словарь данных, передаваемых из view в шаблон.

**Директивы (переменные)** — `{{ variable }}` — вывод значений.

**Теги** — `{% tag %}` — управляющие конструкции (`for`, `if`, `block` и т.д.).

**Фильтры** — `{{ value|filter }}` — преобразование данных перед выводом (например, `|date:"Y-m-d H:i:s"`).

**Админка Django** — готовый интерфейс для управления моделями. Для доступа создаётся суперпользователь (`createsuperuser`).

**ModelAdmin** — класс для тонкой настройки отображения модели в админке (`list_display`, `list_display_links`, `search_fields` и др.).

**Meta** — внутренний класс модели для настройки (`verbose_name`, `verbose_name_plural`, `ordering`).

---

## Выполнение работы

### 1. Вывод данных модели в браузер (без шаблонов)

В `news/views.py` импортируем модель и получаем все новости:

```python
from .models import News

def index(request):
    news = News.objects.all()
    res = '<h1>Список новостей</h1>'
    for item in news:
        res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
    return HttpResponse(res)
```

Данные выводятся, но без стандартных HTML-тегов. Код контроллера быстро разрастается.

### 2. Создание шаблонов

Django ищет шаблоны в папке `templates` приложения. Рекомендуемая структура:

```
news/
└── templates/
    └── news/
        └── index.html
```

### 3. Рендеринг шаблона

Используем функцию `render` из `django.shortcuts`:

```python
from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)
```

### 4. Директивы, теги и фильтры

В шаблоне используются:
- `{{ title }}`, `{{ item.title }}` — директивы
- `{% for item in news %} ... {% endfor %}` — тег цикла
- `{{ item.created_at|date:"Y-m-d H:i:s" }}` — фильтр даты

### 5. Локализация и форматирование даты

**Способ 1** — изменить язык в `settings.py`:

```python
LANGUAGE_CODE = 'ru'
```

**Способ 2** — фильтр даты (более гибкий):

```html
<p>{{ item.created_at|date:"Y-m-d H:i:s" }}</p>
```

### 6. Сортировка новостей

Через `Meta` модели (предпочтительнее):

```python
class Meta:
    ordering = ['-created_at']
```

Тогда в view достаточно `News.objects.all()`.

### 7. Работа с админкой Django

Админка доступна по адресу: http://127.0.0.1:8000/admin/

Создание суперпользователя:

```bash
python manage.py createsuperuser
```

### 8. Регистрация модели в админке

В `news/admin.py`:

```python
from django.contrib import admin
from .models import News

admin.site.register(News)
```

### 9. Настройка Meta и verbose_name

В модели:

```python
class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ['-created_at']
```

В `apps.py`:

```python
verbose_name = 'Новости'
```

### 10. Настройка отображения в админке (ModelAdmin)

```python
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(News, NewsAdmin)
```

### 11. Валидация и миграции

Поле `photo` сделано необязательным (`blank=True`). После изменений модели:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Структура проекта

```
django-lab3/
├── README.md
├── requirements.txt
└── MySite/
    ├── manage.py
    ├── MySite/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    └── news/
        ├── admin.py
        ├── apps.py
        ├── models.py
        ├── views.py
        ├── urls.py
        ├── templates/
        │   └── news/
        │       └── index.html
        └── migrations/
```

---

## Код ключевых файлов

### news/views.py
```python
from django.shortcuts import render
from .models import News

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', context)
```

### news/templates/news/index.html
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>

    {% for item in news %}
        <div>
            <p><strong>{{ item.title }}</strong></p>
            <p>{{ item.content }}</p>
            <p>{{ item.created_at|date:"Y-m-d H:i:s" }}</p>
        </div>
        <hr>
    {% endfor %}
</body>
</html>
```

### news/admin.py
```python
from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register(News, NewsAdmin)
```

### news/models.py
```python
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
```

---

## Проверка работоспособности

1. Создать и активировать venv, установить зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate   # или venv\Scripts\activate на Windows
   pip install -r requirements.txt
   ```
2. Перейти в папку `MySite` и применить миграции:
   ```bash
   cd MySite
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Запустить сервер:
   ```bash
   python manage.py runserver
   ```
4. Открыть:
   - http://127.0.0.1:8000/news/ — список новостей из шаблона
   - http://127.0.0.1:8000/admin/ — админ-панель

---

## Контрольные вопросы

**1. Что такое шаблон в Django и зачем он нужен?**  
HTML-файл с синтаксисом DTL. Отделяет представление от бизнес-логики и позволяет переиспользовать разметку.

**2. Что такое рендеринг и функция `render`?**  
Процесс формирования HTML-страницы из шаблона + контекста. `render(request, template_name, context)` возвращает готовый `HttpResponse`.

**3. Чем отличаются директивы, теги и фильтры?**  
- Директивы `{{ }}` — вывод значений  
- Теги `{% %}` — логика (циклы, условия)  
- Фильтры `|` — преобразование данных перед выводом

**4. Зачем нужна папка `templates/news/` внутри приложения?**  
Для пространства имён. Предотвращает конфликты шаблонов с одинаковыми именами из разных приложений.

**5. Как создать суперпользователя?**  
```bash
python manage.py createsuperuser
```

**6. Как зарегистрировать модель в админке?**  
```python
admin.site.register(News)
# или с настройками:
admin.site.register(News, NewsAdmin)
```

**7. Для чего нужны `verbose_name` и `verbose_name_plural`?**  
Для человекочитаемых названий модели в единственном и множественном числе в админке.

**8. Что делает `list_display` и `search_fields`?**  
`list_display` — какие поля показывать в списке объектов.  
`search_fields` — по каким полям работает поиск.

**9. Зачем нужен атрибут `blank=True`?**  
Разрешает оставлять поле пустым при валидации формы (в админке и не только).

**10. Какие команды используются для миграций после изменения модели?**  
```bash
python manage.py makemigrations
python manage.py migrate
```

