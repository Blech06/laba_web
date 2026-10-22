from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """
    Контроллер главной страницы приложения news.
    Соответствует методичке: функция index.
    """
    # Для отладки можно раскомментировать:
    # print(dir(request))
    # print(request.method, request.path)

    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Новости — Главная</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }
            h1 { color: #1a73e8; }
            a { color: #1a73e8; }
            .card { background: #f5f5f5; padding: 20px; border-radius: 8px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Добро пожаловать на новостной сайт!</h1>
        <div class="card">
            <p>Это страница <strong>index</strong> приложения <code>news</code>.</p>
            <p>Маршрут: <code>/news/</code></p>
            <p><a href="/news/test/">Перейти на страницу test →</a></p>
        </div>
        <hr>
        <p><small>Лабораторная работа №1 — Django. Контроллеры и маршруты.</small></p>
    </body>
    </html>
    """
    return HttpResponse(html)


def test(request):
    """
    Контроллер тестовой страницы.
    Соответствует методичке: функция test.
    """
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Новости — Test</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }
            h1 { color: #0d904f; }
            a { color: #1a73e8; }
            .card { background: #e8f5e9; padding: 20px; border-radius: 8px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <h1>Страница Test</h1>
        <div class="card">
            <p>Это страница <strong>test</strong> приложения <code>news</code>.</p>
            <p>Маршрут: <code>/news/test/</code></p>
            <p>Метод запроса: <code>{}</code></p>
            <p>Путь: <code>{}</code></p>
            <p><a href="/news/">← Вернуться на главную</a></p>
        </div>
        <hr>
        <p><small>Лабораторная работа №1 — Django. Контроллеры и маршруты.</small></p>
    </body>
    </html>
    """.format(request.method, request.path)
    return HttpResponse(html)
