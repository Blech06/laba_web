# Лабораторная работа №2 (Django). Модели. CRUD

**Студент:** [ФИО]  
**Группа:** [Группа]  
**Вариант:** 4 — Задачи (To-Do)  

---

## Цель работы
Разработка моделей, научиться проводить миграцию данных, работа с базой данных.

---

## Теоретическое обоснование (кратко)

**Модель** — класс, наследуемый от `django.db.models.Model`, соответствующий таблице в БД.  
**Миграции** — способ Django отслеживать изменения структуры таблиц (`makemigrations` / `migrate`).  
**ORM** — взаимодействие с БД через Python-код: `create`, `all`, `filter`, `get`, `save`, `delete`.

---

## Выполнение

### 1. Модель News (из методички)

```python
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
```

### 2. Модель Task (Вариант 4)

```python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.IntegerField(default=1)
    category = models.CharField(max_length=50, blank=True, default='')  # доп. поле
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = '✓' if self.is_completed else '○'
        return f'{status} [{self.priority}] {self.title}'
```

### 3. Миграции

```bash
python manage.py makemigrations news
python manage.py migrate
```

Файл миграции уже подготовлен: `news/migrations/0001_initial.py`.

### 4. Настройка медиафайлов

В `settings.py`:
```python
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

В корневом `urls.py`:
```python
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 5. Регистрация в админке

Модели `News` и `Task` зарегистрированы в `admin.py` с `list_display`, фильтрами и поиском.

### 6. Работа с ORM (CRUD) через shell

```bash
python manage.py shell
```

Примеры (см. также `shell_examples.py`):

```python
from news.models import News, Task

# CREATE
News.objects.create(title='Новость 1', content='Текст')
Task.objects.create(title='Сделать лабу', priority=1, category='Учёба')

# READ
News.objects.all()
News.objects.filter(is_published=True)
Task.objects.filter(is_completed=False).order_by('priority')  # требование варианта 4
News.objects.get(id=1)
News.objects.exclude(is_published=False)

# UPDATE
t = Task.objects.get(title='Сделать лабу')
t.priority = 2
t.save()

# DELETE
# News.objects.filter(is_published=False).delete()
```

### 7. Суперпользователь

```bash
python manage.py createsuperuser
```

Админка: http://127.0.0.1:8000/admin/

---

## Как запустить

```bash
unzip django-lab2-models-crud.zip
cd django-lab2
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
cd MySite
python manage.py migrate
python manage.py createsuperuser  # по желанию
python manage.py runserver
```

| URL | Описание |
|-----|----------|
| http://127.0.0.1:8000/news/ | Главная (новости + невыполненные задачи) |
| http://127.0.0.1:8000/admin/ | Админка |

---

## Ответы на контрольные вопросы

1. **Модель** — класс Python, описывающий структуру таблицы БД и предоставляющий ORM-интерфейс.
2. **Типы полей:** CharField, TextField, IntegerField, BooleanField, DateTimeField, ImageField и др.
3. **blank=True** — поле может быть пустым в формах; **null=True** — в БД допускается NULL.
4. **Миграции** — файлы, описывающие изменения схемы. `makemigrations` создаёт, `migrate` применяет.
5. **Суперпользователь:** `python manage.py createsuperuser`.
6. **ORM** — Object-Relational Mapping. CRUD: `create`/`save`, `all`/`filter`/`get`, изменение + `save`, `delete`.
7. **filter()** возвращает QuerySet (0..N записей); **get()** — один объект или исключение.
8. **Медиафайлы:** `MEDIA_ROOT`, `MEDIA_URL` + `static()` в urls.py при DEBUG.
9. **`__str__`** — строковое представление объекта (удобно в админке и shell).
10. **Только makemigrations** — файлы миграций появятся, но таблицы в БД не изменятся, пока не выполнить `migrate`.

---

## Вывод

Созданы модели News (по методичке) и Task (вариант 4). Выполнены миграции, настроена работа с медиафайлами, продемонстрированы все CRUD-операции через Django shell и админку. Реализована фильтрация невыполненных задач с сортировкой по приоритету.

---

## Источники

1. Django Models — https://docs.djangoproject.com/en/4.2/topics/db/models/
2. Migrations — https://docs.djangoproject.com/en/4.2/topics/migrations/
3. QuerySets — https://docs.djangoproject.com/en/4.2/ref/models/querysets/
4. File uploads — https://docs.djangoproject.com/en/4.2/topics/files/
