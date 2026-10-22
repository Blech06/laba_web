"""
Примеры работы с ORM через Django shell.
Запуск: python manage.py shell < ../shell_examples.py
или копировать команды по одной в python manage.py shell
"""

from news.models import News, Task
from django.utils import timezone
from datetime import timedelta

# ========== CREATE (Новости) ==========
n1 = News(title='Новость 1', content='Контент новости 1')
n1.save()

n2 = News.objects.create(title='Новость 2', content='Контент новости 2')
News.objects.create(title='Новость 3', content='Ещё одна новость', is_published=False)

# ========== CREATE (Задачи — вариант 4) ==========
Task.objects.create(title='Сделать лабораторную', description='Django Models CRUD', priority=1, category='Учёба')
Task.objects.create(title='Купить продукты', priority=3, category='Быт', is_completed=False)
Task.objects.create(title='Сдать отчёт', priority=1, category='Учёба', deadline=timezone.now() + timedelta(days=2))
Task.objects.create(title='Позвонить другу', priority=5, category='Личное', is_completed=True)

# ========== READ ==========
print('=== Все новости ===')
print(list(News.objects.all()))

print('=== Опубликованные ===')
print(list(News.objects.filter(is_published=True)))

print('=== Невыполненные задачи по приоритету ===')
print(list(Task.objects.filter(is_completed=False).order_by('priority')))

print('=== get() ===')
print(News.objects.get(id=1))

print('=== exclude() ===')
print(list(News.objects.exclude(is_published=False)))

# ========== UPDATE ==========
task = Task.objects.get(title='Купить продукты')
task.priority = 2
task.save()
print('Обновлён приоритет:', task)

# ========== DELETE ==========
# News.objects.filter(is_published=False).delete()  # раскомментировать при необходимости

print('Готово. CRUD-операции выполнены.')
