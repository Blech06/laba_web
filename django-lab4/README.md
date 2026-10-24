# Лабораторная работа №4: Связи моделей. Внешний вид шаблона

**Студент:** Мержоев Ислам Игоревич  
**Группа:** ПИЖ-б-о-25-1  
**Вариант:** 4  
**Технология:** Python + Django  

## Содержание

- [Цель работы](#цель-работы)
- [Теоретическое обоснование](#теоретическое-обоснование)
- [Выполнение практического примера (News + Category)](#выполнение-практического-примера-news--category)
- [Выполнение индивидуального задания (Вариант 4)](#выполнение-индивидуального-задания-вариант-4)
- [Структура проекта](#структура-проекта)
- [Код ключевых файлов](#код-ключевых-файлов)
- [Проверка работоспособности](#проверка-работоспособности)
- [Контрольные вопросы](#контрольные-вопросы)
- [Вывод](#вывод)
- [Список использованных источников](#список-использованных-источников)

---

## Цель работы

Освоить создание и настройку связей между моделями Django (ForeignKey, ManyToManyField, OneToOneField), изучить параметры связей (`on_delete`, `related_name`, `null`, `blank`, `default`), научиться применять миграции при добавлении связей к существующим моделям, а также настраивать отображение связанных данных в административной панели Django.

---

## Теоретическое обоснование

В Django связи между моделями реализуются специальными полями:

| Тип связи | Класс | Описание |
|-----------|-------|----------|
| Многие-к-одному | `ForeignKey` | Много записей вторичной модели ссылаются на одну запись первичной |
| Многие-ко-многим | `ManyToManyField` | Записи связаны через промежуточную таблицу |
| Один-к-одному | `OneToOneField` | Одна запись соответствует ровно одной другой |

**Важные параметры ForeignKey:**
- `on_delete` — поведение при удалении связанного объекта (`CASCADE`, `PROTECT`, `SET_NULL`, `RESTRICT` и др.)
- `null=True` — разрешить NULL в БД
- `blank=True` — разрешить пустое значение в формах
- `related_name` — имя обратной связи
- `verbose_name` — человекочитаемое название поля

**Почему нужна нормализация:**  
Хранить название категории в каждой новости — нарушение нормализации. При переименовании категории пришлось бы обновлять все записи. Выносим категории в отдельную таблицу и связываем через внешний ключ.

---

## Выполнение практического примера (News + Category)

### 1. Создание модели Category

```python
class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
```

### 2. Добавление ForeignKey в модель News

```python
category = models.ForeignKey(
    Category,
    on_delete=models.PROTECT,
    null=True,
    verbose_name='Категория'
)
```

- `on_delete=models.PROTECT` — запрещает удаление категории, если на неё ссылаются новости
- `null=True` — необходимо, потому что в таблице уже есть записи

### 3. Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Настройка админки

```python
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
```

---

## Выполнение индивидуального задания (Вариант 4)

**Тема:** Университет — студенты и группы

| Компонент | Описание |
|-----------|----------|
| Первичная модель | `Group` (название, курс, специальность) |
| Вторичная модель | `Student` (имя, фамилия, номер зачётки, email) |
| Тип связи | `ForeignKey` (одна группа — много студентов) |
| on_delete | `SET_NULL` (при удалении группы студент остаётся, но без группы) |
| Дополнительно | `null=True` для поля группы |

### Модели

```python
class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название группы')
    course = models.PositiveSmallIntegerField(verbose_name='Курс')
    specialty = models.CharField(max_length=150, verbose_name='Специальность')

    def __str__(self):
        return f'{self.title} ({self.course} курс)'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['title']


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    record_book = models.CharField(max_length=20, unique=True, verbose_name='Номер зачётки')
    email = models.EmailField(verbose_name='Email')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='Группа'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']
```

### Админка

```python
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'specialty')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'specialty')
    list_filter = ('course',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'record_book', 'email', 'group')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name', 'record_book', 'email')
    list_filter = ('group', 'group__course')
```

---

## Структура проекта

```
django-lab4/
├── README.md
├── requirements.txt
├── .gitignore
└── MySite/
    ├── manage.py
    ├── MySite/
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── news/                    # Пример из методички
    │   ├── models.py            # Category + News
    │   ├── admin.py
    │   ├── views.py
    │   └── templates/news/
    └── university/              # Индивидуальное задание (вариант 4)
        ├── models.py            # Group + Student
        ├── admin.py
        └── apps.py
```

---

## Код ключевых файлов

### news/models.py
```python
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']
```

### university/models.py
```python
from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название группы')
    course = models.PositiveSmallIntegerField(verbose_name='Курс')
    specialty = models.CharField(max_length=150, verbose_name='Специальность')

    def __str__(self):
        return f'{self.title} ({self.course} курс)'

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['title']


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    record_book = models.CharField(max_length=20, unique=True, verbose_name='Номер зачётки')
    email = models.EmailField(verbose_name='Email')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students',
        verbose_name='Группа'
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']
```

### news/admin.py
```python
from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
```

### university/admin.py
```python
from django.contrib import admin
from .models import Group, Student


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course', 'specialty')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'specialty')
    list_filter = ('course',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'record_book', 'email', 'group')
    list_display_links = ('id', 'last_name')
    search_fields = ('last_name', 'first_name', 'record_book', 'email')
    list_filter = ('group', 'group__course')


admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
```

---

## Проверка работоспособности

1. Создать venv и установить зависимости:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. Применить миграции:
   ```bash
   cd MySite
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   ```
3. Запустить сервер:
   ```bash
   python manage.py runserver
   ```
4. Открыть http://127.0.0.1:8000/admin/
5. Создать категории и привязать к новостям
6. Создать группы и студентов, проверить `SET_NULL` (удалить группу — студент остаётся без группы)

---

## Контрольные вопросы

**1. Какие типы связей существуют в Django?**  
ForeignKey (многие-к-одному), ManyToManyField (многие-ко-многим), OneToOneField (один-к-одному).

**2. Что делает `on_delete=models.PROTECT`?**  
Запрещает удаление объекта, на который есть ссылки (выбрасывает ProtectedError).

**3. Что делает `on_delete=models.SET_NULL`?**  
При удалении связанного объекта поле устанавливается в NULL (требуется `null=True`).

**4. Зачем нужен `null=True` при добавлении ForeignKey к существующей таблице?**  
Потому что в таблице уже есть записи, и СУБД не сможет заполнить обязательное поле значением.

**5. Что такое `related_name`?**  
Имя обратной связи. Например, `group.students.all()` вместо `group.student_set.all()`.

**6. Чем `blank=True` отличается от `null=True`?**  
`null` — уровень БД, `blank` — уровень валидации форм.

**7. Зачем нужен `db_index=True`?**  
Создаёт индекс в БД для ускорения поиска и фильтрации.

**8. Как настроить фильтры в админке?**  
Атрибут `list_filter = ('field1', 'field2')` в классе ModelAdmin.

**9. Как сделать поле редактируемым прямо в списке админки?**  
`list_editable = ('field',)`.

**10. Почему при `default=1` возникла ошибка целостности?**  
В таблице Category не было записи с id=1, а миграция пыталась проставить это значение существующим новостям.

---
