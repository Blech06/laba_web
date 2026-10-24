# Лабораторная работа №5: Внешний вид шаблона. Директивы. Теги. Фильтры

**Студент:** Мержоев Ислам Игоревич  
**Группа:** ПИЖ-б-о-25-1  
**Вариант:** 4  
**Технология:** Python + Django + Bootstrap  

## Содержание

- [Цель работы](#цель-работы)
- [Теоретическое обоснование](#теоретическое-обоснование)
- [Выполнение работы](#выполнение-работы)
  - [1. Подключение Bootstrap через CDN](#1-подключение-bootstrap-через-cdn)
  - [2. Navbar](#2-navbar)
  - [3. Карточки новостей (Card)](#3-карточки-новостей-card)
  - [4. Вывод категории и вызов метода модели](#4-вывод-категории-и-вызов-метода-модели)
  - [5. Тег cycle](#5-тег-cycle)
  - [6. forloop.counter](#6-forloopcounter)
  - [7. Тег now](#7-тег-now)
  - [8. Вывод изображений и фильтры](#8-вывод-изображений-и-фильтры)
- [Структура проекта](#структура-проекта)
- [Код ключевых файлов](#код-ключевых-файлов)
- [Проверка работоспособности](#проверка-работоспособности)
- [Контрольные вопросы](#контрольные-вопросы)
- [Вывод](#вывод)
- [Список использованных источников](#список-использованных-источников)

---

## Цель работы

Улучшить внешний вид шаблона с помощью Bootstrap, освоить директивы, теги и фильтры Django Template Language, научиться выводить связанные данные, изображения и применять встроенные теги (`cycle`, `now`, `forloop`).

---

## Теоретическое обоснование

**Bootstrap** — бесплатный HTML/CSS/JS-фреймворк для быстрой адаптивной вёрстки. Подключается через CDN без скачивания файлов.

**CDN (Content Delivery Network)** — сеть серверов, обеспечивающая быструю доставку статического контента.

**Директивы** — `{{ variable }}` — вывод значений.

**Теги** — `{% tag %}` — управляющие конструкции:
- `{% for %}` / `{% endfor %}`
- `{% if %}` / `{% else %}` / `{% endif %}`
- `{% cycle %}` — чередование значений
- `{% now %}` — текущая дата/время
- `forloop.counter` — номер текущей итерации

**Фильтры** — `{{ value|filter }}`:
- `|date:"Y-m-d H:i:s"` — форматирование даты
- `|truncatewords:50` — обрезка текста
- `|linebreaks` — переносы строк
- `|safe` — вывод HTML без экранирования

В шаблоне можно вызывать методы модели: `{{ item.my_func }}`.

---

## Выполнение работы

### 1. Подключение Bootstrap через CDN

Берём Starter template с [getbootstrap.com](https://getbootstrap.com/docs/5.3/getting-started/introduction/) и подключаем CSS/JS через CDN.

### 2. Navbar

Добавляем навигационную панель Bootstrap с ссылками «Главная» и «Добавить новость».

### 3. Карточки новостей (Card)

Каждая новость выводится в компоненте Card:
- header — категория + метод модели
- body — заголовок, контент, кнопка, изображение
- footer — дата создания

### 4. Вывод категории и вызов метода модели

В модели `News` добавлен метод:

```python
def my_func(self):
    return 'Последние новости'
```

В шаблоне: `{{ item.my_func }}` и `{{ item.category }}`.

### 5. Тег cycle

```html
<h5 class="card-title {% cycle 'text-danger' 'text-success' %}">
```

Чередует красный/зелёный цвет заголовков.

### 6. forloop.counter

```html
{{ forloop.counter }}
```

Выводит порядковый номер новости (начиная с 1).

### 7. Тег now

```html
{% now 'Y-m-d H:i:s' %}
```

Отображает текущую дату и время.

### 8. Вывод изображений и фильтры

```html
{% if item.photo %}
    <img src="{{ item.photo.url }}" ...>
{% else %}
    <img src="https://picsum.photos/..." ...>
{% endif %}
```

Контент с фильтрами: `{{ item.content|safe|linebreaks|truncatewords:50 }}`

---

## Структура проекта

```
django-lab5/
├── README.md
├── requirements.txt
├── .gitignore
└── MySite/
    ├── manage.py
    ├── MySite/
    ├── news/
    │   ├── models.py          # + метод my_func
    │   ├── admin.py
    │   ├── views.py
    │   └── templates/news/
    │       └── index.html     # Bootstrap-шаблон
    └── university/            # из ЛР №4 (вариант 4)
```

---

## Код ключевых файлов

### news/models.py (фрагмент)
```python
class News(models.Model):
    # ... поля ...
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def my_func(self):
        return 'Последние новости'

    def __str__(self):
        return self.title
```

### news/templates/news/index.html
```html
<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>{{ title }}</title>
</head>
<body>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
        <a class="navbar-brand" href="/">Navbar</a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav">
                <li class="nav-item"><a class="nav-link" href="/news/">Главная</a></li>
                <li class="nav-item"><a class="nav-link" href="/admin/">Добавить новость</a></li>
            </ul>
        </div>
    </div>
</nav>

<div class="container mt-3">
    <h1>{{ title }}</h1>
    {% now "Y-m-d H:i:s" %}
    <div class="row">
        <div class="col-md-12">
            {% for item in news %}
            <div class="card mb-3">
                <div class="card-header">
                    {{ forloop.counter }}. {{ item.my_func }} | Категория: {{ item.category }}
                </div>
                <div class="card-body">
                    <div class="d-flex">
                        {% if item.photo %}
                            <img src="{{ item.photo.url }}" alt="" width="350" class="me-3">
                        {% else %}
                            <img src="https://picsum.photos/id/1060/350/235/?blur=2" alt="" class="me-3">
                        {% endif %}
                        <div>
                            <h5 class="card-title {% cycle 'text-danger' 'text-success' %}">{{ item.title }}</h5>
                            <p class="card-text">{{ item.content|safe|linebreaks|truncatewords:50 }}</p>
                            <a href="#" class="btn btn-primary">Read more...</a>
                        </div>
                    </div>
                </div>
                <div class="card-footer text-muted">
                    {{ item.created_at|date:"Y-m-d H:i:s" }}
                </div>
            </div>
            {% empty %}
                <p>Новостей пока нет.</p>
            {% endfor %}
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## Проверка работоспособности

1. Установить зависимости и применить миграции:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   cd MySite
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
2. Открыть http://127.0.0.1:8000/news/
3. В админке добавить новости с категориями, текстом и (опционально) фото
4. Убедиться, что:
   - Navbar отображается
   - Карточки чередуют цвет заголовка
   - Выводится номер, метод `my_func`, категория, дата
   - Изображения показываются (или placeholder)

---

## Контрольные вопросы

**1. Что такое Bootstrap и зачем он нужен?**  
HTML/CSS/JS-фреймворк для быстрой адаптивной вёрстки.

**2. Что такое CDN?**  
Сеть серверов для быстрой доставки статического контента.

**3. Чем отличаются директивы, теги и фильтры?**  
Директивы `{{ }}` — вывод; теги `{% %}` — логика; фильтры `|` — преобразование.

**4. Что делает тег `{% cycle %}`?**  
Поочерёдно подставляет переданные значения (удобно для чередования стилей).

**5. Что такое `forloop.counter`?**  
Номер текущей итерации цикла (начиная с 1).

**6. Как вывести текущую дату в шаблоне?**  
`{% now "Y-m-d H:i:s" %}`

**7. Как вызвать метод модели из шаблона?**  
`{{ item.method_name }}` (метод без аргументов, кроме `self`).

**8. Как вывести изображение из ImageField?**  
`{{ item.photo.url }}` (при наличии файла).

**9. Что делают фильтры `truncatewords`, `linebreaks`, `safe`?**  
Обрезка текста, переносы строк, вывод HTML без экранирования.

**10. Зачем нужен `{% empty %}` в цикле for?**  
Выводит содержимое, если queryset пуст.

---

## Вывод

В ходе лабораторной работы:

1. Подключён Bootstrap через CDN.
2. Создан современный шаблон с Navbar и карточками новостей.
3. Освоены директивы, теги (`for`, `if`, `cycle`, `now`) и фильтры.
4. Реализован вывод связанных данных (категория), вызов метода модели, изображений.
5. Применены `forloop.counter` и чередование стилей через `cycle`.

Шаблон стал адаптивным и визуально привлекательным.

---

## Список использованных источников

1. [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
2. [Django Template Language](https://docs.djangoproject.com/en/stable/ref/templates/language/)
3. [Встроенные теги и фильтры Django](https://docs.djangoproject.com/en/stable/ref/templates/builtins/)
4. Методические указания к лабораторной работе №5
