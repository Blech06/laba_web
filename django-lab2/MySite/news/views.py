from django.http import HttpResponse
from django.shortcuts import render
from .models import News, Task


def index(request):
    """Главная страница приложения news."""
    news_list = News.objects.filter(is_published=True)
    tasks = Task.objects.filter(is_completed=False).order_by('priority')

    html = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Новости и Задачи</title>
        <style>
            body {{ font-family: Arial, sans-serif; max-width: 900px; margin: 30px auto; padding: 20px; }}
            h1, h2 {{ color: #1a73e8; }}
            .card {{ background: #f8f9fa; padding: 16px; border-radius: 8px; margin: 12px 0; }}
            .task {{ border-left: 4px solid #0d904f; }}
            .done {{ opacity: 0.6; text-decoration: line-through; }}
            a {{ color: #1a73e8; }}
        </style>
    </head>
    <body>
        <h1>Новостной сайт + Задачи (Вариант 4)</h1>
        <p><a href="/news/test/">Страница test</a> | <a href="/admin/">Админка</a></p>

        <h2>Опубликованные новости ({news_list.count()})</h2>
        {''.join(f'<div class="card"><strong>{n.title}</strong><br><small>{n.created_at}</small><br>{n.content[:200]}</div>' for n in news_list) or '<p>Нет новостей</p>'}

        <h2>Невыполненные задачи (по приоритету) — {tasks.count()}</h2>
        {''.join(f'<div class="card task"><strong>[{t.priority}] {t.title}</strong> <em>({t.category})</em><br>{t.description}<br><small>Срок: {t.deadline or "не указан"}</small></div>' for t in tasks) or '<p>Все задачи выполнены!</p>'}
    </body>
    </html>
    """
    return HttpResponse(html)


def test(request):
    return HttpResponse('<h1>Страница test</h1><p><a href="/news/">← Назад</a></p>')
