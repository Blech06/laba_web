from django.db import models


class News(models.Model):
    """
    Модель новостей (из методички лабораторной работы №2).
    """
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        null=True,
        verbose_name='Фото'
    )
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class Task(models.Model):
    """
    Вариант 4. Задачи (To-Do).
    Поля: title, description, deadline, is_completed, priority + category.
    """
    title = models.CharField(max_length=200, verbose_name='Название задачи')
    description = models.TextField(blank=True, verbose_name='Описание')
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения')
    is_completed = models.BooleanField(default=False, verbose_name='Выполнена')
    priority = models.IntegerField(default=1, verbose_name='Приоритет')
    category = models.CharField(max_length=50, blank=True, default='', verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')

    def __str__(self):
        status = '✓' if self.is_completed else '○'
        return f'{status} [{self.priority}] {self.title}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['priority', 'deadline']
